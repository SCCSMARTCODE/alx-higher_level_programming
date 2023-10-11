#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    f_set = ((my_list[0][0] * my_list[0][1]) + (my_list[1][0] * my_list[1][1]))
    s_set = ((my_list[2][0] * my_list[2][1]) + (my_list[3][0] * my_list[3][1]))
    d_set = ((my_list[0][1] + my_list[1][1]) + (my_list[2][1] + my_list[3][1]))
    return (f_set + s_set) / d_set
