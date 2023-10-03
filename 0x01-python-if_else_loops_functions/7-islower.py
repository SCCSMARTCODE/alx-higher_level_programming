#!/usr/bin/python3
def islower(c):

    if c != str(c) or len(str(c)) == 0:
        return Error
    ch = 'a'
    while ch <= 'z':
        if c == ch:
            return True
        ch = chr(ord(ch) + 1)

    return False
