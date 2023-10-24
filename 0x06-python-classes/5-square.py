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
        
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for size.
        Returns:
            int: The size of the square.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): The size to set.

        Raises:
            ValueError: If value is not a positive integer.
            TypeError: if value is not an integer.

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        my_print:
            it print out the square with # character.
            if my __size == 0 print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print("")

    def area(self):
        """
        This method returns the current square area
        """
        return self.__size ** 2
