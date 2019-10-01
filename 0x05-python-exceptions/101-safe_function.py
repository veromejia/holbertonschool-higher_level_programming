#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as fct_error:
        print("Exception: {}".format(fct_error), file=sys.stderr)
        return None
