#!/usr/bin/env python3

def no_c(my_string):

    n_string = ''
    for x in my_string:
        if x not in ('c', 'C'):
            n_string += x

    return n_string
