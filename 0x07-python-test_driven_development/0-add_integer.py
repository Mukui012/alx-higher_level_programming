#!/usr/bn/python3
"""
Defines module add_integer with two parameters
"""


def add_integer(a, b=98):
    """
    Returns value of a + b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
