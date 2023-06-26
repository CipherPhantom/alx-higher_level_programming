#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except Exception as err:
        result = None
        print("Exception: {}".format(err), file=sys.stderr)
    return result
