#!/usr/bin/python3


"""Square Class

This module defines a simple Square class that can be used to
represent squares in your Python programs.

Usage Example:

    # Import the Square class
    Square = __import__('#-square').Square

    # Create an instance of the Square class
    my_square = Square()

    # Display the type of the object and its dictionary
    print(f"Type of my_square: {type(my_square)}")
    print(f"Dictionary of my_square: {my_square.__dict__}")

The Square class is a basic blueprint for creating square objects.
providing a foundation for further customization and use in your projects.
The example demonstrates how to create an instance
of the Square class and inspect its type and dictionary.

"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """An object constructor method.

        Initiatilizes Square with size.

        Arg:
            size: A integer representing object size.
                  Has a default value of 0.
            position: A position definer

        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter method for position.
        Returns:
            int: To retrieve position value.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position.

        Args:
            value (tuple): The size to set.

        Raises:
            TypeError: position must be a tuple of 2 positive integers

        """
        v = value

        if not isinstance(v, tuple) or v[0] < 0 or v[1] < 0 or len(v) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        my_print:
            it print out the square with # character.
            if my __size == 0 print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        if self.__position[1] != 0:
            print("" * self.__position[1])
        else:
            pass

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print("")

    def area(self):
        """
        This method returns the current square area
        """
        return self.__size ** 2
