#!/usr/bin/python3
"""
function that returns True if the object is an instance of a class
that's inherited from the specified class
"""


def inherits_from(obj, a_class):
    """returns True is obj is instance
    false otherwise"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
