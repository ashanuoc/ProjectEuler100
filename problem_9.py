""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2
    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc."""

import math

a = 1
b = 2

while True:
    num = a + b + math.sqrt(a**2 + b**2)
    if num < 1000:
        b = b + 1
    elif num == 1000:
        print('a*b*c =', a * b * math.sqrt(a**2 + b**2))
        print(b)
        break
    else:
        a = a + 1  # a < b < c
        b = a + 1

