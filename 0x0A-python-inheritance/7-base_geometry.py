#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Reperesents a geometric shape"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if input is an integer

        Args:
            name (str): The name of the paremeter
            value (int): The value of the parameter

        Raises:
            TypeError: If `value` is not integer
            ValueError: If `value` is less than or equal to zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
