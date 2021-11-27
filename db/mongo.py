#! /usr/local/bin/python

import os
import pymongo


class MongoDB:
    DB = os.environ.get('MONGO_DB', None)
    COL = os.environ.get('MONGO_COLLECTION', None)

    MONGO_USER = os.environ.get('MONGO_USER', None)
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', None)

    client = pymongo.MongoClient(host='mongodb', username=MONGO_USER, password=MONGO_PASSWORD, authSource='admin')
    db = client[DB]
    collection = db[COL]

    def insert(self, data: dict):
        return self.collection.insert_one(data)
