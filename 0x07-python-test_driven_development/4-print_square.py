#!/usr/bin/python3
"""
A module that contains a  function that prints square

tests:
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
"""


def print_square(size):
    """
    print_square - print a square of length - > size

    para:
        size
    print(square)
    """
    i = 0
    j = 0

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    while i < size:
        while j < size:
            print("#", end="")
            j += 1
        print("")
        j = 0
        i += 1
