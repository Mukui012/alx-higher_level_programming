#!/usr/bin/python3
"""Definition of a locked class"""


class LockedClass:
    """Only allows for attribute first_name"""
    __slots__ = ["first_name"]
