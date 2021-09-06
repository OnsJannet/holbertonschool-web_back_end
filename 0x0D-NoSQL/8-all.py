#!/usr/bin/env python3
""" List all documents in Python """

from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all documents in a collection """
    cursor = mongo_collection.mycollection
    for document in cursor.find():
        if document is None:
            return ([])
        else:
            return (document)
