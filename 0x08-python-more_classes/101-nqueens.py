#!/usr/bin/python3
"""
This is a module thatb solve the:
    10. N queens
"""
import sys


def is_valid(board, row, col, n):
    """Check if it's safe to place a queen in the given position"""
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n):
    """Recursively find all solutions to the N-Queens problem"""
    if row == n:
        # Found a solution, print it
        for i in range(n):
            print("".join(["Q" if cell == 1 else "." for cell in board[i]]))
        print()
        return

    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n)
            board[row][col] = 0


def nqueens(n):
    """Main function to solve the N-Queens problem"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solve_nqueens(board, 0, n)


if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
