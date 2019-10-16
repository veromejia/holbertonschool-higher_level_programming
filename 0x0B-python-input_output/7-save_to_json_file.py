#!/usr/bin/python3
"""Module to write an object's JSON representation to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """returns the object represented by a JSON string)"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
