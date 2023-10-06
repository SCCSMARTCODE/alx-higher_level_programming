#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    min_no = 0
    for x in my_list:
        if min_no > x:
            min_no = x
    max_no = min_no
    for x in my_list:
        if max_no < x:
            max_no = x
    return(max_no)
