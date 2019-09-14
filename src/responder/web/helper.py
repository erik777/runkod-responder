import os

from flask import request


def get_project_name() -> str:
    return os.environ.get('TEST_PROJECT') or request.host
