#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d_list = list(a_dictionary.keys())
    for x in d_list:
        if a_dictionary[x] == value:
            del a_dictionary[x]
    return a_dictionary
