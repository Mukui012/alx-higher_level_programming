#!/usr/bin/python3
""" Takes in a letter and sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""
if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    request = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        request_dict = request.json()
        id = request_dict.get('id')
        name = request_dict.get('name')
        if len(request_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(request_dict.get('id'), request_dict.get('name')))
    except:
        print("Not a valid JSON")
