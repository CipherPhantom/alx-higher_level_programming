#!/usr/bin/python3
"""Defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'.

    Args:
        filename (str): The name of file.

    Returns:
        obj (any): A Python object.
    """
    with open(filename, encoding='utf-8') as fp:
        obj = json.load(fp)
    return obj
