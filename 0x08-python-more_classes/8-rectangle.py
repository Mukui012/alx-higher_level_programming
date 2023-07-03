#!/usr/bin/python3
"""
class Rectangle with attributes width and height
"""


class Rectangle():
    """
    Definition of class rectangle
    Args:
        int width
        int height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes rectangles """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ Deletes instance of the class """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ prints diagram of rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """ str representation to create new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
