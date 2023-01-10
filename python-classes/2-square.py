#!/usr/bin/python3
"""Square class started from here"""


class Square:
    """This class creates
    An empty class and
    this is my first class"""
    def __init__(self, size=0):
        if size not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
