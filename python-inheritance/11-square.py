#!/usr/bin/python3
"""Mahesh"""


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Mahesh"""
    def __init__(self, size):
        """Mahesh"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Mahesh"""
        return (self.__size * self.__size)
    
    def __str__(self):
        """Mahesh"""
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
