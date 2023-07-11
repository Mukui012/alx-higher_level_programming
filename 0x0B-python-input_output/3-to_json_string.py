#!/usr/bin/python3
"""Function that returns JSON representaton
of an object(string)"""
import json


def to_json_string(my_obj):
    """Returns JSON representation"""
    return json.dumps(my_obj)
