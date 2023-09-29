#!/usr/bin/python3
"""Sends a POST request to a given URL with an email """
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value_pair = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value_pair).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
