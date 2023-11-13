#!/usr/bin/python3
"""this is a module that contain the Rectangle class
        inheriting from the mother(Base class)
"""
from models.base import Base


def type_mark(val, typ, message):
    """

    :param val:
    :param typ:
    :param message:
    :return:
    """
    if not isinstance(val, typ):
        raise TypeError("{} must be an integer".format(message))


def size_mark(val, no=0, message=""):
    """

    :param val:
    :param no:
    :param message:
    :return:
    """
    if val <= 0:
        if no == 0:
            raise ValueError("{} must be > 0".format(message))
        raise ValueError("{} must be >= 0".format(message))


class Rectangle(Base):
    """The rectangle class
            this is a child that inherit from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """

        :param width:
        :param height:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        type_mark(self.__height, int, "height")
        size_mark(self.__height, 0, "height")
        size_mark(self.__width, 0, "width")
        type_mark(self.__width, int, "width")
        type_mark(self.__x, int, "x")
        size_mark(self.__x + 1, 1, "x")
        type_mark(self.__y, int, "y")
        size_mark(self.__y + 1, 1, "y")

    @property
    def width(self):
        """

        :return: width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        :param width:
        :return:
        """
        self.__width = width
        size_mark(self.__width, 0, "width")
        type_mark(self.__width, int, "width")

    @property
    def height(self):
        """
        :return: __height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        :param height:
        :return:
        """
        self.__height = height
        type_mark(self.__height, int, "height")
        size_mark(self.__height, 0, "height")

    @property
    def x(self):
        """
        :return: __x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        :param x:
        :return:
        """
        self.__x = x
        type_mark(self.__x, int, "x")
        size_mark(self.__x + 1, 1, "x")

    @property
    def y(self):
        """
        :return: __y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        :param y:
        :return:
        """
        self.__y = y
        type_mark(self.__y, int, "y")
        size_mark(self.__y + 1, 1, "y")

    def area(self):
        """
        :return: area value
        """
        return self.__width * self.__height

    def display(self):
        """
        display or printing the rectangle
        :return:
        """
        for _ in range(self.y):
            print("")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        attribute_names = ["id", "width", "height", "x", "y"]

        # Update attributes using *args
        for i, value in enumerate(args):
            setattr(self, attribute_names[i], value)

        # Update attributes using **kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        :return: [{}] ({}) {}/{} - {}/{}
        """
        return "[{}] ({}) {}/{} - {}/{}".format("Rectangle", self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self):
        """
        :return: my_dict
        """
        my_dict = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
        return my_dict
