import os
from flask import request
import mimetypes
from typing import Optional


def get_project_name():
    return os.environ.get('TEST_PROJECT') or request.host


def resolve_path(p: str) -> Optional[str]:
    r = p

    # add slash to beginning
    if not r.startswith('/'):
        r = '/{}'.format(r).strip()

    # root path
    if r == '/':
        return '/index.html'

    # if path has a know mime type
    if mimetypes.guess_type(r):
        return r

    return r
