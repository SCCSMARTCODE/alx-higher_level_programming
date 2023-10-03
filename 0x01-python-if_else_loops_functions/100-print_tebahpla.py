#!/usr/bin/python3
changer = 1
alpha = 'z'

while alpha >= 'a':
    if changer % 2 == 0:
        print(alpha.upper(), end = "")
    else:
        print(alpha, end = "")
    changer += 1
    alpha = chr(ord(alpha) - 1)
