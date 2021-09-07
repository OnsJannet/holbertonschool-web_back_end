#!/usr/bin/env python3
"""  returns the list of school
having a specific topic """

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    collection = mongo_collection
    topic = collection.find({"topics": topic})
    return topic
