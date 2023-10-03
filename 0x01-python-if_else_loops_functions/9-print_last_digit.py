def print_last_digit(number):
    if number < 0:
        number = abs(number)
    l_di = number % 10
    print(l_di, end = "")
    return l_di
