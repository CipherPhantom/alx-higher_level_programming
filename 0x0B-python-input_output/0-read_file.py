#!/usr/bin/python3
"""Defines a read_file function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file.
    """
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            print(line, end="")
