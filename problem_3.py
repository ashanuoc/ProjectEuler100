# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(number) :
    x = number
    i = 2

    while i <= number :
        while number%i == 0 :
            number = number/i
            max_prime = i
            

        i = i+1

    return print('largest prime factor of the number ', x, ' = ', max_prime)

largest_prime_factor(600851475143)