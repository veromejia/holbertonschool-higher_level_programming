#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response"""


import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email_dic = {'email': argv[2]}
    data = urllib.parse.urlencode(email_dic)
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
