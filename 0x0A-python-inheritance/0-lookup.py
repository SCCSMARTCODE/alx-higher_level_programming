#!/usr/bin/python3
"""Module for the lookup function
Finding a list of available attributes and methods of an object.
"""


def lookup(obj):
    """Returns that list of attributes and methods of an object.
        You are not allowed to import any module

    Args:
        - obj: object to look into
    """
    return dir(obj)
