#!/usr/bin/python3
"""Module that defines class Student"""


class Student:
    """Definition of class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation"""
        return self.__dict__
