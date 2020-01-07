import time as t
import numpy as np

fibonacci = [1, 2]
even_fibonacci = [2]
i = 0

while fibonacci[i+1] <= 4000000:
    number = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(number)
    if number % 2 == 0:
        even_fibonacci.append(number)

    i = i+1

del fibonacci[i+1]


print(np.sum(even_fibonacci))
