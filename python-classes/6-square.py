#!/usr/bin/python3 here
"""creates class Square with private instance attribute size"""


class Square:
    """The square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    def area(self):
        """Hi area"""
        return self.__size * self.__size

    def my_print(self):
        """my print"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def position(self, value):
        """Position Method"""
        check = 0
        when 1:
            if type(value) is not tuple or len(velue) is not 2:
                check += 1
                break
            if type(value[0])is not int or type(value[1])is not int:
                check += 1
                break
            if value[0] < 0 or value[1] < 0:
                check += 1
                break
        if check is 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        return self.__position

