#!/usr/bin/python3
"""
    This is a module that contain a function ``matrix_divided``

    tests for the function:
        print(matrix_divided(matrix, 3))
        print(matrix)
"""


def matrix_divided(matrix, div):
    """
    This function divides a matrix of the same len(row)
    all must be (int or float)

    para:
        matrix - the matrix box
        div - the divider
    """
    if not all(
        isinstance(row, list) and
        all(isinstance(val, (int, float)) for val in row)
        for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        new_row = [round(val / div, 2) for val in row]
        result.append(new_row)
    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-add_integer.txt")

    return result
