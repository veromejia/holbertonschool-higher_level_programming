#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure (list,
    dictionary, string, integer, boolean) for JSON serialization of an object
    """
    return obj.__dict__
