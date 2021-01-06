""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million. """

num = 205

for n in range(2, num):
    s = num%n
    print('n',n)
    if s == 0:
        print('not a prime')
        break

