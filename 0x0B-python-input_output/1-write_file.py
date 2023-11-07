#!/usr/bin/python3
"""This module contains
     a function that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """This module Write a function that writes a string
            to a text file (UTF8)
        Return:
             the number of characters written:
             """
    with open(filename, 'w') as f:
        return f.write(text)
