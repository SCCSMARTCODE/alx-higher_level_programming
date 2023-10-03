def uppercase(str):
    ch = 'a'
    
    while ch <= 'z':
        if ch in str:
           str = str.replace(ch, chr(ord(ch) -32))
        ch = chr(ord(ch) + 1)
    print(str)
    return 1
