#!/usr/bin/python3
"""
Defining class MyList that inherits from class list
"""


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
