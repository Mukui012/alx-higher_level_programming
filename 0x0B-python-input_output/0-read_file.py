#!/usr/bin/python3


def read_file(filename=""):
    with open("my_file_0.txt", mode='r', encoding='utf-8') as a_file:
        print(a_file.read())