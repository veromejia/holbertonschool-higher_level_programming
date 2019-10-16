#!/usr/bin/python3
"""module for read_lines"""


def read_lines(filename="", nb_lines=0):
    """Read n lines of a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        lnumber = 0
        for line in f:
            if lnumber < nb_lines or nb_lines <= 0:
                print(line, end="")
            lnumber += 1
