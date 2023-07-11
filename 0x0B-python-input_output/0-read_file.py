#!/usr/bin/python3
"""Function that reads a text file and prints to stdout"""


def read_file(filename=""):
    """Function definition"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end="")
