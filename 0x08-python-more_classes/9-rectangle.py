#!/usr/bin/python3
"""
Class Rectangle with private attributes width and height
"""


class Rectangle():
    """
    Definition of a class Rectangle
    Args:
        int width
        int height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ Deletes instance of class """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width"""
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
        """ prints rectangle with symbol # """
        if self.__width == 0 or self.__height == 0:
            return ""
        diag = "\n".join([str(self.print_symbol) * self.__width
            for rows in range(self.__height)])
        return diag

    def __repr__(self):
        """ String representation to create new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns a rectangle with bigger area"""
        if not isinstance(rect_1, Rectangle) or \
                not isinstance(rect_2, Rectangle):
            raise TypeError("{} must be an instance of Rectangle".
                            format("rect_1" if not
                                isinstance(rect_1, Rectangle)
                                else "rect_2"))
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Returns new rectangle instance with width == height == size """
        return cls(size, size)
