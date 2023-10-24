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
    """Defines the blueprint of a square.

    Attribute:
        size: An integer indicating the size of the square object.
    """

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

        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
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

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def area(self):
        """
        This method returns the current square area
        """
        return self.__size ** 2
