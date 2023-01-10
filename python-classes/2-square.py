#!/usr/bin/python3 here
"""creates class Square with private instance attribute size"""


class Square:
    """This class creates
    An empty class and
    this is my first class"""
    def __init__(self, size=0):
        """Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
