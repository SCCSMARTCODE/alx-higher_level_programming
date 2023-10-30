#!/usr/bin/python3
"""
This is a module thatb solve the:
    10. N queens
"""

from sys import argv


def solve_nqueens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j]:
                return False
        return True

    def solve(board, col):
        if col >= n:
            sos.append([[i, row.index(1)] for i, row in enumerate(board)])
            return
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    sos = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return sos


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
        sos = solve_nqueens(n)
        for solution in sos:
            print(solution)
    except ValueError:
        print("N must be a number")
        exit(1)
