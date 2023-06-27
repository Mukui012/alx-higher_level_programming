#!/usr/bin/python3

"""Defines class Square"""


class Square:
    """
    Represents a square
    Args:
        __size: size of a side of a square
    """

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
