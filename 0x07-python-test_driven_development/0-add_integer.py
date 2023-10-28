#!/usr/bin/python3
"""A module that contain add_integer function
    tests:
        print(add_integer(1, 2))
        print(add_integer(100, -2))
        print(add_integer(2))
        print(add_integer(100.3, -2))
        try:
            print(add_integer(4, "School"))
        except Exception as e:
            print(e)
        try:
            print(add_integer(None))
        except Exception as e:
            print(e)

"""


def add_integer(a, b=98):
    """Add integer a function that add parameter

    parameter:
        a: first arg to be int
        b: default value 98
    Raises:
        TypeError: if type(a) or type(b) is not int or float
    Return:
        int(a) + int(b)
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
