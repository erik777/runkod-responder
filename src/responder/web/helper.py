import os

from flask import request


def get_project_name() -> str:
    print(request.host)
    return os.environ.get('TEST_PROJECT') or request.host
