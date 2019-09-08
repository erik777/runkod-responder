import os
from flask import Flask, abort, redirect

from werkzeug.middleware.proxy_fix import ProxyFix
from runkod.util import assert_env_vars
from runkod.helper import get_project_name, resolve_path

import requests
from runkod.db import get_project, get_file

app = None


def __flask_setup():
    global app

    app = Flask(__name__, static_folder=None)
    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

    app.wsgi_app = ProxyFix(app.wsgi_app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):

        project_name = get_project_name()

        project = get_project(project_name)

        if project is None:
            abort(404)

        full_path = resolve_path(path)

        rec = get_file(project, full_path)

        if rec is None:
            abort(404)

        serve_file = full_path.endswith('index.html')

        address = rec['address']

        if serve_file:
            resp = requests.get(address)

            return resp.text
        else:
            return redirect(address, code=308)


def __run_dev_server():
    global app

    app.config['DEVELOPMENT'] = True
    app.config['DEBUG'] = True

    app.run(host='127.0.0.1', port=8088)


__flask_setup()


def main():
    assert_env_vars('TEST_PROJECT')
    __run_dev_server()
