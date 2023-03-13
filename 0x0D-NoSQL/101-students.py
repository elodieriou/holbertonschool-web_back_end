#!/usr/bin/env python3
""" pymongo module """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    top_student = [
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"},
        }},
        {"$sort": {"averageScore": -1}}
    ]

    results = mongo_collection.aggregate(top_student)
    return results
