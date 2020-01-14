#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter."""


import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
        q_data = {'q': q}
    else:
        q = ""

    r = requests.post("http://0.0.0.0:5000/search_user", data=q_data)
    try:
        my_dic = r.json()
        if my_dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(my_dic.get('id'), my_dic.get('name')))
    except ValueError:
        print('Not a valid JSON')
