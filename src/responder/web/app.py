import os
import tempfile

import requests
from flask import Flask, abort, make_response, redirect
from flask_caching import Cache
from werkzeug.middleware.proxy_fix import ProxyFix

from responder.db import get_project, get_file
from responder.helper import resolve_path
from responder.util import assert_env_vars
from responder.web.helper import get_project_name

app = None
cache = None


def __flask_setup():
    global app, cache

    app = Flask(__name__, static_folder=None)
    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

    app.wsgi_app = ProxyFix(app.wsgi_app)

    cache_config = {'CACHE_TYPE': 'filesystem', 'CACHE_THRESHOLD': 10000,
                    'CACHE_DIR': os.path.join(tempfile.gettempdir(), 'responder')}
    cache = Cache(with_jinja2_ext=False, config=cache_config)
    cache.init_app(app)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        project = get_project(get_project_name())

        if project is None:
            abort(404)

        file_path = resolve_path(project, path)

        file = get_file(project, file_path)

        if file is None:
            abort(404)

        rv = cache.get(file['name'])
        if rv is None:
            resp = requests.get(file['address'])
            rv = resp.content
            cache.set(file['name'], rv)

        response = make_response(rv)
        if file['type']:
            response.headers.set('Content-Type', file['type'])

        return response


def __run_dev_server():
    global app

    app.config['DEVELOPMENT'] = True
    app.config['DEBUG'] = True

    app.run(host='127.0.0.1', port=8088)


__flask_setup()


def main():
    assert_env_vars('TEST_PROJECT')
    __run_dev_server()
