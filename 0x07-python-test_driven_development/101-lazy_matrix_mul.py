#!/usr/bin/python3
"""Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """This function multiplies the two parameter
        and return value using Numpy
    """
    return numpy.matmul(m_a, m_b)
