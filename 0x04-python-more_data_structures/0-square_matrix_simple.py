#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []

    for row in matrix:
        new_row = []  # Create a new row for the result matrix
        for element in row:
            new_row.append(element ** 2)  # Square each element and append to the new row
        new.append(new_row)  # Append the new row to the result matrix

    return new

