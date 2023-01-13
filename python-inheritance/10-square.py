#!/usr/bin/python3
"""Mahesh"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Mahesh"""
    def __init__(self, size):
        """Mahesh"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        """Mahesh"""
        return (self.__size * self.__size)
