#!/usr/bin/python3


def uniq_add(my_list=[]):
    new = list(my_list)
    # remove repetition in list
    for i in new:
        j = 0
        ne = i
        for i in new:
            if i == ne:
                del new[j]
            j += 1
        new.append(ne)
    sum = 0
    for x in new:
        sum += x
    return sum
