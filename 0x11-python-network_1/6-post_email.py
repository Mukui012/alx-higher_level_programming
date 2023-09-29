#!/usr/bin/python3
""" Sends a POST request to a given URL with a given email """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value_pair = {"email": sys.argv[2]}

    req = requests.post(url, data=value_pair)
    print(req.text)
