#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    errors = (ValueError, TypeError, ZeroDivisionError, IndexError)
    try:
        result = fct(args[0], args[1])
    except errors as err:
        result = None
        print("Exception: {}".format(err), file=sys.stderr)
    return result
