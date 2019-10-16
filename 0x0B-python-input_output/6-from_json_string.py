#!/usr/bin/python3
"""Module that Return an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """ Return an obj (Python data structure) represented by a JSON string"""
    return (json.loads(my_str))
