#!/usr/bin/python3
"""Defines a write_file function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
        returns the number of characters written.

        Args:
            filename (str): The name of the file.
            text (str): The text to write to the file.

        Returns:
            n_char (int): The number of characters.
    """
    with open(filename, mode="w", encoding="utf-8") as fp:
        n_char = fp.write(text)
    return n_char
