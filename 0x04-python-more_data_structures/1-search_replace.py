#!/usr/bin/python3

def search_replace(my_list, search, replace):
    i = 0
    new_list = list(my_list)
    for x in my_list:
        if x == search:
            new_list[i] = replace
        i += 1
    return new_list
