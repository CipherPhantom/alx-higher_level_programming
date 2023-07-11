#!/usr/bin/python3
"""Defines a save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (any): The object.
        filename (str): The name of the file.
    """
    with open(filename, mode="w", encoding="utf-8") as fp:
        json.dump(my_obj, fp)
