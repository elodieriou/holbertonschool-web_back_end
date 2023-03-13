#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    number_logs = nginx_collection.count()
    print("{} logs".format(number_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_document = nginx_collection.find({"method": method})
        count_method = method_document.count()
        print("method {}: {}".format(method, count_method))

    status_check = nginx_collection.find({"method": "GET", "path": "/status"})
    count_status_check = status_check.count()
    print("{} status check".format(count_status_check))
