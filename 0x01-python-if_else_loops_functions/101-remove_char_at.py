def remove_char_at(str, n):
    if n > len(str):
        return str
    elif n < 0:
        return str
    str = str.replace(str[n], "")
    return str