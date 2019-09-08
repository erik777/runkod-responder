import mimetypes
from typing import Optional


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
