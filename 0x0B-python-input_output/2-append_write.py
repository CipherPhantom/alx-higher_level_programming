#!/usr/bin/python3
"""Defines a append_write function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
        returns the number of characters added.

        Args:
            filename (str): The name of the file.
            text (str): The text to write to the file.

        Returns:
            n_char (int): The number of characters.
    """
    with open(filename, mode="a", encoding="utf-8") as fp:
        n_char = fp.write(text)
    return n_char
