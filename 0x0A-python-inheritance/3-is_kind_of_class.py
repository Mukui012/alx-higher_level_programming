#!/usr/bin/python3
"""
Module that checks if an object is an instance
of a class """


def is_kind_of_class(obj, a_class):
    """function that checks if an object is an
    instance of a class
    True if obj is an instance, false otherwis
    """
    return isinstance(obj, a_class)
