#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    l_di = number % 10
    print("{}".format(l_di), end="")
    return l_di
