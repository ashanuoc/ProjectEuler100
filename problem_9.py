""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2
    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc."""

import math

maxInt = math.floor(math.sqrt(1000))  # Find the largest natural number that its square close to 1000

print(maxInt)
