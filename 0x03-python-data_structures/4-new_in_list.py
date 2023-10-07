#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 > idx or idx > (len(my_list) - 1):
        return my_list
    else:
        n_list = my_list.copy()
        n_list[idx] = element
        return n_list
