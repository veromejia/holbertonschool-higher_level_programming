#!/usr/bin/python3

"""
Takes your Github credentials (username and password) and uses the
Github API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if "json" not in req.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        json_file = req.json()
        print(json_file.get('id'))
