#!usr/bin/python3
"""Class that defines a Square from class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Definition """

    def __init__(self, size):
        """ Method that initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns area """
        return super().area()

    def __str__(self):
        """ method that returns a string """
        return "[Square] {}/{}".format(self.__size, self.__size)
