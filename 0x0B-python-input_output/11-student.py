#!usr/bin/python3
"""Module that defines class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializes instance of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation"""
        my_dict = dict()
        if type(attrs) is list and all(type(i is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    my_dict.update({i: self.__dict__[i]})
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces all attributes of Student"""
        for x in json:
            self.__dict__.update({x: json[x]})
