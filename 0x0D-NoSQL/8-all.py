#!/usr/bin/env python3
""" pymongo module """


def list_all(mongo_collection):
    """ List all documents in Python """
    documents = mongo_collection.find()
    if not documents:
        return []
    return documents
