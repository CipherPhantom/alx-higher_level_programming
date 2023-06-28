#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.__size == other.size
        return False

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.__size != other.size
        return False

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.__size > other.size
        return False

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.__size >= other.size
        return False

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.__size < other.size
        return False

    def __le__(self, other):
        if isinstance(other, Square):
            return self.__size <= other.size
        return False