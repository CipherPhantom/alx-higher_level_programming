#!/usr/bin/python3
"""Defines a find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    n = len(list_of_integers)
    if n == 0:
        return None
    return max(list_of_integers)
