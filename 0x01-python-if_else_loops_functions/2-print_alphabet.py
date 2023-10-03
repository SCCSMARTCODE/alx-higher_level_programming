#!/usr/bin/python3
x = 'a'
while x <= 'z':
    print(x, end = "")
    x = chr(ord(x) + 1)
