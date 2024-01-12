#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
    server = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = server.logs.nginx

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")
    get = nginx_collection.count_documents({"method": "GET"})
    print(f"\tmethod GET: {get}")
    post = nginx_collection.count_documents({"method": "POST"})
    print(f"\tmethod POST: {post}")
    put = nginx_collection.count_documents({"method": "PUT"})
    print(f"\tmethod PUT: {put}")
    patch = nginx_collection.count_documents({"method": "PATCH"})
    print(f"\tmethod PATCH: {patch}")
    delete = nginx_collection.count_documents({"method": "DELETE"})
    print(f"\tmethod DELETE: {delete}")
    status = nginx_collection.count_documents({"method": "GET"},
                                              {"path": "/status"})
    print(f"{status} status check")
