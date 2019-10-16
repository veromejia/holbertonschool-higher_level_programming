#!/usr/bin/python3
"""Module to write a file"""


def write_file(filename="", text=""):
    """Write a string to a text file and returns
    the number of characters written"""
    with open(filename, mode="w") as f:
        return f.write(text)
