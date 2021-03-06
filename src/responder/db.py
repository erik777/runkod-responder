import os
from typing import Optional

import pymongo

client = pymongo.MongoClient(os.environ.get('MONGO_URI'))

db = client.get_default_database()


def get_project(project_name: str) -> Optional[dict]:
    filters = {'radiksType': 'project', 'name': project_name, 'deleted': False}
    return db['radiks-server-data'].find_one(filters, sort=[('createdAt', pymongo.DESCENDING)])


def get_redirected_project(project: dict) -> Optional[dict]:
    filters = {'radiksType': 'project', '_id': project['redirectTo'], 'signingKeyId': project['signingKeyId'],
               'deleted': False}
    return db['radiks-server-data'].find_one(filters, sort=[('createdAt', pymongo.DESCENDING)])


def get_file(project: dict, path: str) -> Optional[dict]:
    filters = {'radiksType': 'file', 'project': project['_id'], 'signingKeyId': project['signingKeyId'],
               'tag': project['tag'], 'fullPath': path, 'deleted': False}
    return db['radiks-server-data'].find_one(filters, sort=[('createdAt', pymongo.DESCENDING)])
