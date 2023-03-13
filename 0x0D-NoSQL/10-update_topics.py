#!/usr/bin/env python3
""" pymongo module """


def update_topics(mongo_collection, name, topics):
    """ Change school topics """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)
