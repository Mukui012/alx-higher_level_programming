#!/usr/bin/python3
"""Function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """Function definition"""
    with open(filename, mode='a+', encoding="utf-8") as file:
        return file.write(text)
