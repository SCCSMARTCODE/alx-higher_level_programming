#!/usr/bin/python3
"""this is a rectangle module
Usage in code:
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)

"""


class Rectangle:
    """rectangle class:
        this is a blue print for rectangle classes of all cases

        Attribute:
            width: An integer indicating the width of the rectangle object.
            height: An integer indicating the height of the rectangle object.


    """
    def __init__(self, width=0, height=0):
        """this is the class initializer"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """the width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """the width setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0@property")

        self.__width = value

    @property
    def height(self):
        """The height getter"""
        return self.__height

    @height.setter
    """the height setter"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
