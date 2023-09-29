#!/usr/bin/python3
""" Python script that takes in a URL """

if __name__ == "__main__":
    import urllib.request as request
    from sys import arg
    req = request.Request(arg[1])
    with request.urlopen(req) as response:
        print(r.headers.get('X-Request-Id'))
