#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list == []:
        return None
    m_no = my_list[0]
    for x in my_list:
        if x > m_no:
            m_no = x
    return m_no
