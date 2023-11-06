#!/usr/bin/python3
"""Module for the function 1-my_list
    this will Creates a class inheriting from the list class.
"""


class MyList(list):
    """Class MyList inherits from list

            no __init__
    """

    def print_sorted(self):
        """Prints the list, in ascending format
        print("{}".format(new_list))

        """

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
