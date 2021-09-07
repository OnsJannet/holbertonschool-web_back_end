#!/usr/bin/env python3
"""  changes all topics of a school
document based on the name """

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    collection = mongo_collection
    updated = collection.update_many({"name": name},
                                     {"$set": {"topics": topics}})
    return updated
