#!/usr/bin/env python3                                                              
""" pymongo module """


def insert_school(mongo_collection, **kwargs):
    """ Insert a document in python """
    documents = mongo_collection.insert(kwargs)
    return documents
