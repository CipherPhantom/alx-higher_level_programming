#!/usr/bin/python3
"""Defines a from_json_string function."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
        represented by a JSON string.

    Args:
        my_str (str): The JSON string.
    """
    return json.loads(my_str)
