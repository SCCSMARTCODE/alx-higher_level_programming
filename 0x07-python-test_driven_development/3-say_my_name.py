#!/usr/bin/python3
"""
This module is containing:
    say_my_name function:
        para:
            first_name
            last_name
        print("My name is {} {}".format(first_name, last_name))
"""


def say_my_name(first_name, last_name=""):
    """
    a function that:
    gets para:
        first_name
        last_name
    print("My name is {} {}".format(first_name, last_name))
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
