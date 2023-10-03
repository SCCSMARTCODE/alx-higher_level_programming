#!/usr/bin/python3

val = 0
val2 = 0

while val <= 9:
    while val2 <= 9:
        if val2 > val:
            if val != 8:
                print("{}{}".format(val, val2), end=", ")
            else:
                print("{}{}".format(val, val2))
        val2 += 1
    val2 = 0
    val += 1
