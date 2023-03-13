#!/usr/bin/env python3
""" pymongo module """


def schools_by_topic(mongo_collection, topic):
    """ Return the list of school having a specific topic """
    documents = mongo_collection.find({"topics": topic})
    return documents
