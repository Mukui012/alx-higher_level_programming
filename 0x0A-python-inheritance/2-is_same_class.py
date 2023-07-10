#!/usr/bin/python3
"""
Module that checks if an object is an instance
of a class"""


def is_same_class(obj, a_class):
    """Definition of module is_same_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
