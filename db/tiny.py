#! /usr/local/bin/python

import os
from tinydb import TinyDB, Query
from tinydb.operations import delete


class MyTinyDB:

    TINYDB_URL = os.environ.get('TINYDB_URL', None)

    if TINYDB_URL:
        db_url = '/code/tinydb/db.json'
    else:
        db_url = 'db.json'

    db = TinyDB(db_url)
    query = Query()

    def get(self, data: dict):
        return self.db.search(Query().fragment(data))

    def insert(self, data: dict):
        return self.db.insert(data)

    def all(self):
        return self.db.all()

    def update(self, data):
        self.db.update(delete('crawled'), Query().fragment(data))
