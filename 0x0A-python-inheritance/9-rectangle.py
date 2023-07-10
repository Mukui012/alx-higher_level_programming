#!/usr/bin/python3
"""class that defines a rectangle from BaseGeometry Class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Definition"""

    def __init__(self, width, height):
        """ Initializes instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method that returns area"""
        return self.__width * self.__height

    def __str__(self):
        """method that returns the string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
