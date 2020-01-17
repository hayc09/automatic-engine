#!/usr/bin/env python3

from math import gcd as denom, isclose
from random import randrange


def gcd(a, b):
    """Function takes in two values, compares them, setting largest value to a,
    and smallest to b, performs Euclid's algorithm until the remainder is zero,
    returning the largest common denominator"""
    rem = 1
    while rem != 0:
        c = 1
        if a > b:
            large = a
            small = b
        else:
            large = b
            small = a
        dif = small + 1
        while dif > small:
            dif = large - c * small
            c += 1
        rem = large - (c - 1) * small
        if rem > 0:
            a = small
            b = dif
    return small


if __name__ == "__main__":
    rand1 = randrange(0, 1000, 1)
    rand2 = randrange(0, 1000, 1)
    x = gcd(rand1, rand2)
    y = denom(rand1, rand2)
    z = isclose(x, y)
    print('The largest common denominator for the random numbers ' + str(rand1) + ' and ' + str(rand2) + ' is: ')
    print(str(x) + ' from my function and ' + str(y) + " from python's built in function")

