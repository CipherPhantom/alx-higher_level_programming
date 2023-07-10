#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Reperesents a geometric shape"""

    def area(self):
        """Raises an exception if function is not implemented

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if input is an integer

            Raises:
                TypeError: If `value` is not integer
                ValueError: If `value` is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
