#!/usr/bin/python3
""" Solving the N queens puzzle """
import sys


def solvequeen(n: int) -> None:
    """ Solving the N queens puzzle """
    board = [-1] * n
    addqueen(board, 0)


def addqueen(board: list, row: int) -> None:
    """ Recursive function to add queens on the board """
    if row == len(board):
        solution = []
        for i in range(len(board)):
            solution.append([i, board[i]])

        print(solution)
        return

    board[row] = -1

    while (board[row] < len(board) - 1):
        board[row] += 1
        if isvalid(board, row):
            addqueen(board, row + 1)


def isvalid(board: list, row: int) -> bool:
    """ Check if placing a queen at this position is valid """
    for i in range(row):
        if board[i] == board[row]:
            return False

        if abs(board[i] - board[row]) == abs(i - row):
            return False

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solvequeen(n)
