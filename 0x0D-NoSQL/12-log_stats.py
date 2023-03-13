#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    number_logs = nginx_collection.count_documents({})
    print("{} logs".format(number_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_method = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count_method))

    count_status_check = nginx_collection.count_documents({"method": "GET",
                                                           "path": "/status"})
    print("{} status check".format(count_status_check))
