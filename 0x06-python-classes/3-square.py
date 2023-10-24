#!/usr/bin/python3

"""Defines a blueprint of a square.

Attribute:
    size: An integer that telles the size of the square.

"""

class Square:
    def __init__(self, size=0):
        """An object constructor method.

        Initiatilizes Square with size.

        Arg:
            size: A integer representing object size.
                  Has a default value of 0.
        
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    def area(self):
        """
        This method returns the current square area
        """
        return self.__size ** 2
