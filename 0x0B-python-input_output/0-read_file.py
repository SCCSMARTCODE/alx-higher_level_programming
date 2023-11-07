#!/usr/bin/python3
"""This is a module that reads
    Abd print a file in python

    """


def read_file(filename=""):
    """This function reads and print"""

    with open(filename) as f:
        reader = f.read()
        print(reader, end="")
