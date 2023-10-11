#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    list_n = new.keys()
    for x in list_n:
        new[x] = new[x] * 2
    return new
