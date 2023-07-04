#!/usr/bin/python3
"""
class Rectangle with attribute width and height
"""


class Rectangle:
    """
    Defines class Rectangle
    Args:
        width
        height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter or 0 if width or height is 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ prints rectangle with # char """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """ str representation to create new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)