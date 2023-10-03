#!/usr/bin/python3

val = 0
if val == 0:
    while val <= 99:
        if val <=9:
            pre = "0"
        else:
            pre = ""
        if val == 99:
            print("{}".format(val))
        else:
            print("{}{}".format(pre, val), end=", ")
        val += 1
