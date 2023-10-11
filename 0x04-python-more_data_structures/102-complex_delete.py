#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d = dict(a_dictionary)
    d_list = list(d.keys())
    for x in d_list:
        if d[x] == value:
            del d[x]
    return d
