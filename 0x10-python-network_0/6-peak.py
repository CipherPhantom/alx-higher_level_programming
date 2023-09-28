#!/usr/bin/python3
"""Defines a find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    left = list_of_integers[:n//2]
    right = list_of_integers[n//2:]
    if find_peak(left) > find_peak(right):
        return find_peak(left)
    else:
        return find_peak(right)
