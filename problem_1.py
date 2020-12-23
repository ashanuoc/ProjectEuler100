# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time as t
import numpy as np


tic = t.time()

n = 1000

total = np.sum(np.arange(0, n, 3)) + np.sum(np.arange(0, n, 5)) - np.sum(np.arange(0, n, 15))

print(total)

toc = t.time()

print(toc - tic)
