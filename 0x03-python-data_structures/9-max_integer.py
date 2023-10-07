#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_no = my_list[0]
    for x in my_list:
        if x > max_no:
            max_no = x
    return(max_no)
