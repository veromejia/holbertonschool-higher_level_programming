#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        print("Exception:", sys.exc_info()[1])
        return False
    return True
