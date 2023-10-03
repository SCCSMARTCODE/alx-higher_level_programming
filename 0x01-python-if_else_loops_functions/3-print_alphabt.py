#!/usr/bin/python3
x = 'a'
while x <= 'z':
    if x != 'q' and x != 'e':
        print("{}".format(x), end="")
        x = chr(ord(x) + 1)
    else:
        x = chr(ord(x) + 1)
