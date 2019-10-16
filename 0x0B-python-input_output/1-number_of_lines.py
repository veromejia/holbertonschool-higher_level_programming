#!/usr/bin/python3
"""Module that gives the number of lines"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    nlines = 0
    with open(filename, 'r') as f:
        for line in f:
            nlines += 1
    return nlines
