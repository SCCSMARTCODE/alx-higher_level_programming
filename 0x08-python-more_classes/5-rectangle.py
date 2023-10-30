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
    """Defines the blueprint of a rectangle.

    Attribute:
        width: An integer indicating the width of the rectangle object.
        height: An integer indicating the height of the rectangle object.
    """

    def __init__(self, width=0, height=0):
        """Class constructor to initialize the Rectangle object.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height

    def __repr__(self):
        """
        this is the repr method to return string for the
            eval functon ti evaluate it
        Return:
            Rectangle({self.__width}, {self.__height})
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        This is the Deleter
            This function is called when any class is deleted
            Noted
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0 (negative).
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0 (negative).
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of the rectangle
        formula:
            width * height
        Return: area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Perimeter of a rectangle
        formula:
            2(h + w)
        Return: perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        str: this will work the return

        Return:
            if any arg is zero
                return ""
            else:
                return #box
        """
        make = ""
        if 0 in (self.__width, self.__height):
            return make
        for i in range(self.__height):
            for j in range(self.__width):
                make += '#'
            make += '\n'
        return make[:-1]
