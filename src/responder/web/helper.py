import os

from flask import request


def get_project_name() -> str:
    return os.environ.get('TEST_PROJECT') or request.host


def can_serve(file: dict) -> bool:
    return file['name'].endswith(('.html', '.css')) and file['size'] <= 1024000
