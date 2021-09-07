#!/usr/bin/env python3
""" List all documents in Python """

from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all documents in a collection """
    documents = mongo_collection.find()
    if not documents:
        return ([])
    else:
        return (documents)
