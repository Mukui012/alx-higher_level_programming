#!/usr/bin/python3

"""Defines class Square with private size and public area"""


class Square:
    """
    class Square definition
    Args:
        size : size of a side of a square
    Functions list:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        print(self)
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get/set current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square
        """
        return (self.__size)**2

    def my_print(self):
        """
        Prints square with #'s
        """
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))
