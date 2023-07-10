#!/usr/bin/python3
"""Defines a add_attribute function"""


def add_attribute(obj, attr_name, attr_value):
    """Adds attribute to an object

    Args:
        obj (`obj`): The object
        attr_name: Attribute_name
        attr_value: Attribute_vale

    Raises:
        TypeError: If the object can’t have new attribute
    """
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)

