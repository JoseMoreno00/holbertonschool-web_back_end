#!/usr/bin/env python3
"""
8. List all documents in Python whit pymongo
"""
import pymongo


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""
    list_docs = mongo_collection.find()
    if list_docs is None:
        return []
    return list_docs
