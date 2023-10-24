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

Feel free to modify and expand upon this class to suit your specific needs.
"""


class Square:
    """Defines the blueprint of a square.

    Attribute:
        size: An integer indicating the size of the square object.
    """
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
