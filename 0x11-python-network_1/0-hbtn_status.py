#!/usr/bin/python3
""" Program that fetches a URL """
import urllib.request


if __name__ == '__main__':
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        page = response.read()
        page_decoded = page.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page_decoded))
