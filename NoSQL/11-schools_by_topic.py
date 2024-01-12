#!/usr/bin/env python3
"""
Function that returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Function"""
    return mongo_collection.find({"topics":topic})
