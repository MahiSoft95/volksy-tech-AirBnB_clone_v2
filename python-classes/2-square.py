#!/usr/bin/python3
"""Square class started from here
raising TypeError and Value Error"""


class Square:
    """This class creates
    An empty class and
    this is my first class"""


    def __init__(self, size=0):
        if type(size) not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
