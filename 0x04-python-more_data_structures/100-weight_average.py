#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    len_s = len(my_list)
    x = 0
    y = 0
    t_sum = 0
    d_sum = 0
    while x < len_s:
        mul = 1
        y = 0
        while y < 2:
            mul *= my_list[x][y]
            if y == 1:
                d_sum += my_list[x][y]
            y += 1
        t_sum += mul
        x += 1
    if t_sum == 0:
        return 0.0

    return t_sum / d_sum
