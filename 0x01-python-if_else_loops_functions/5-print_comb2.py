#!/usr/bin/python3

val = 0
val1 = 0
while val <= 9:
    while val1 <= 9:
        if val == val1 == 9:
            print("{}{}".format(val, val1))
        else:
            print("{}{}".format(val, val1), end=", ")
        val1 += 1
    val1 = 0
    val += 1
