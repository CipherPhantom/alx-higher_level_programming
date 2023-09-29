#!/usr/bin/python3
"""Defines a find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    n = len(list_of_integers)
    mid = n // 2
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and \
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
