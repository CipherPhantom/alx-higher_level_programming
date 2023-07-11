#!/usr/bin/python3
"""Defines a pascal_triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
        the Pascal’s triangle of n.

    Args:
        n (int): The base of the triangle.
    """

    if n <= 0:
        return []
    outer = []
    for i in range(n):
        inner = []
        if i > 0:
            inner.append(1)
        if i > 1:
            for j in range(i-1):
                inner.append(outer[i-1][j] + outer[i-1][j+1])
        inner.append(1)
        outer.append(inner)
    return outer
