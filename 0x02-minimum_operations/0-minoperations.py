#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n: int) -> int:
    """ Minimum Operations """
    if n < 2:
        return 0
    operations = 0
    main = 2
    while main <= n:
        if n % main == 0:
            n /= main
            operations += main
        elif main % 2 == 1:
            main += 2
        else:
            main += 1
    return operations
