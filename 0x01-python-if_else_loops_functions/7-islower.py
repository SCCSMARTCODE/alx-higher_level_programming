#!/usr/bin/python3
def islower(c):
    ch = 'a'
    while ch <= 'z':
        if c == ch:
            return True
        ch = chr(ord(ch) + 1)
        
    return False
