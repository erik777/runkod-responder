import os

import requests
from flask import Flask, abort, redirect, make_response
from werkzeug.middleware.proxy_fix import ProxyFix

from runkod.db import get_project, get_file
from runkod.helper import resolve_path
from runkod.util import assert_env_vars
from runkod.web.helper import get_project_name

app = None


def __flask_setup():
    global app

    app = Flask(__name__, static_folder=None)
    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

    app.wsgi_app = ProxyFix(app.wsgi_app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        project = get_project(get_project_name())

        if project is None:
            abort(404)

        file_path = resolve_path(path)

        file = get_file(project, file_path)

        if file is None:
            abort(404)

        address = file['address']

        serve_flag = file_path.endswith('.html')

        if serve_flag:
            resp = requests.get(address)
            response = make_response(resp.content)
            response.headers.set('Content-Type', file['type'])
            return response

        return redirect(address, 301)


def __run_dev_server():
    global app

    app.config['DEVELOPMENT'] = True
    app.config['DEBUG'] = True

    app.run(host='127.0.0.1', port=8088)


__flask_setup()


def main():
    assert_env_vars('TEST_PROJECT')
    __run_dev_server()
