#!/usr/bin/python3
"""Function that writes a string to a text file
and returns the number of caracters written"""


def write_file(filename="", text=""):
    """Prints string to text file"""
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)
