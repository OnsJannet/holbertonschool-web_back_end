#!/usr/bin/env python3
"""  inserts a new document in a
collection based on kwargs """

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ insert a new documents in a collection """
    collection = mongo_collection
    inserted = collection.insert_one(kwargs)
    return inserted.inserted_id
