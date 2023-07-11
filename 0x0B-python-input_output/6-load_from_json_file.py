#!/usr/bin/python3
"""Function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Function definition"""
    with open(filename, mode='w') as file:
        json.loads(file)
