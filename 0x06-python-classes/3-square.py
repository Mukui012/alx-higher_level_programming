#!/usr/bin/python3

"""Definition of class Square"""


class Square:
    """
    Class sqaure definition
    Args:
        size: size of a size of square
        area: area of a square
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        self.area = area
        area = size * size
        return area
