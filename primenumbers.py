import math


def is_prime(num):
    """Returns True if the number is prime
    else False."""

    if num <= 1:
        """ 0, 1 and negative numbers are not prime numbers.
            Also catered for in the filter function as ange starts from 1
        """
        return False

    if num == 2:
        """ 0, 1 and negative numbers are not prime numbers.
            Also catered for in the filter function as ange starts from 1
        """
        return True

    """ only need to get to square root of inputted max number
        as opposed to going all the way to the last number
        reduces performance time from 0.545s to 0.038s for num as 10000
    """
    limit = int(math.sqrt(num) + 1)

    for x in range(2, limit):   # boost performance by not iterating all numbers
        if num % x == 0:  # not prime if divisible by other numbers
            return False
    else:
        return True


def prime_generator(max_num):
    if max_num < 0:
        return False

    all_primes = [2]

    """ range function skips all even numbers to boost performance"""
    gen_primes = list(filter(is_prime, range(1, max_num+1, 2)))

    all_primes.extend(gen_primes)
    return all_primes


""" testing with 10000
    run "time python3 primenumbers.py
"""
# my_primes = prime_generator(10000)
# print(my_primes)
