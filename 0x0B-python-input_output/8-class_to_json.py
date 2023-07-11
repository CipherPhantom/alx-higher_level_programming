#!/usr/bin/python3
"""Defines a class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure.

    This dictionary will be used for JSON serialization of an object.

    Args:
        obj (any): A Python Object
    """
    return obj.__dict__
