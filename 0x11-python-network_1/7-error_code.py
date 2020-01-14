#!/usr/bin/python3
"""takes in URL, sends request to URL, displays response including errors"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    status = req.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(req.text)
