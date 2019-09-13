import mimetypes
from typing import Optional
from responder.constants import PATH_SEPARATOR, DIR_INDEX, DIR_INDEX_SEARCH_TRY
from responder.db import get_file


def resolve_path(project: dict, p: str) -> Optional[str]:
    r = p

    # add slash to beginning
    if not r.startswith(PATH_SEPARATOR):
        r = '/{}'.format(r).strip()

    # root path
    if r == PATH_SEPARATOR:
        return '{}{}'.format(PATH_SEPARATOR, DIR_INDEX)

    # if path has a known mime type
    if mimetypes.guess_type(r)[0] is not None:
        return r

    s = list(filter(lambda x: x != '', r.split(PATH_SEPARATOR)))

    i = 1
    while True:
        if len(s) == 0:
            path = '{}{}'.format(PATH_SEPARATOR, PATH_SEPARATOR.join(s))
        else:
            path = '{}{}{}'.format(PATH_SEPARATOR, PATH_SEPARATOR.join(s), PATH_SEPARATOR)

        full_path = '{}{}'.format(path, DIR_INDEX)

        f = get_file(project, full_path)
        if f is not None:
            return full_path

        if i == DIR_INDEX_SEARCH_TRY or len(s) == 0:
            break

        s = s[:-1]
        i += 1

    return r
