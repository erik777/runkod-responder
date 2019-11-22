import os

from flask import request

from responder.constants import *


def get_project_name() -> str:
    return os.environ.get('TEST_PROJECT') or request.host


def can_serve(file: dict) -> bool:
    file_ext = file['name'].split('.')[-1].lower()

    return file_ext in FILE_SERVE_RULES and file['size'] <= FILE_SERVE_RULES[file_ext]
