#!/usr/bin/python3
""" Island Parameter """


def island_perimeter(grid):
    """ Island Parameter """
    pram = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:

                if i == 0 or grid[i - 1][j] == 0:
                    pram += 1

                if i + 1 == len(grid) or grid[i + 1][j] == 0:
                    pram += 1

                if j + 1 == len(grid[i]) or grid[i][j + 1] == 0:
                    pram += 1

                if j == 0 or grid[i][j - 1] == 0:
                    pram += 1

    return pram
