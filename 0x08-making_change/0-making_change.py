#!/usr/bin/python3
""" The coin change """
import heapq


def makeChange(coins, total):
    """ Returns the fewest number of coins needed to meet total """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    return num_coins if total == 0 else -1
