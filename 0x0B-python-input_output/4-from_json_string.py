#!/usr/bin/python3
"""Function that returns an object represented
by JSON string"""
import json


def from_json_string(my_str):
    """Decoding the object"""
    return json.loads(my_str)
