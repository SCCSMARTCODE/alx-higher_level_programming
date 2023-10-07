#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    i = 0
    j = 0

    if matrix == [[]]:
        print("")
    while i < len(matrix):

        while j < len(matrix[i]):
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
            j += 1

        j = 0
        i += 1
