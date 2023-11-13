#!/usr/bin/python3
"""this module contains the class Square which is also
        inheriting from Rectangle and Rectangle from Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The grand child class Square
        :param
            Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        :param size:
        :param x:
        :param y:
        :param id:
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        :return: ___
        """
        return "[{}] ({}) {}/{} - {}".format(
                "Square",
                self.id,
                self.x,
                self.y,
                self.size
            )

    @property
    def size(self):
        """
        :return: self.__width
        """
        return self.__width

    @size.setter
    def size(self, val):
        """
        :param val:
        :return: ___
        """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")

        self.__width = val
        self.__height = val

    def update(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return: ___
        """
        attribute_names = ["id", "size", "x", "y"]

        # Update attributes using *args
        for i, value in enumerate(args):
            setattr(self, attribute_names[i], value)

        # Update attributes using **kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        :return: my_dict
        """
        my_dict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return my_dict
