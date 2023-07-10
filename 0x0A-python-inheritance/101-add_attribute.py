#!/usr/bin/python3
""" Function that adds a new attribute to an object"""


def add_attribute(obj, name, value):
    """ Function Definition
    Raises:
        TypeError: when the attribute can't be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
