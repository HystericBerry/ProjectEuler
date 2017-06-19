"""
Problem 3
Title:    Largest Prime Factor
Author:   Paul Kim
Date:     6/19/2017

Description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

# returns a set of primes less than N (exclusive)
def primeSieve(N):
    cache = [True]*N

    count = range(2, N)
    for i in count:
        if i*i <= N:
            for j in count:
                idx = j*i
                if idx < N:
                    cache[idx] = False
                else:
                    break
        else:
            break

    primes = []
    for i in range(2, N):
        if cache[i]:
            primes.append(i)

    return primes

def largetPrimeFactor(num):
    N = int(math.ceil(math.sqrt(num)))
    # reverse the primes
    primes = primeSieve(N)[::-1]
    for i in primes:
        if num%i == 0:
            return i

    return -1

#####MAIN METHOD#####
format = "Largest prime factor of %d! is: %d."

num = 13195
lpf = largetPrimeFactor(num)
print(format % (num, lpf))

# Largest prime factor of 13195! is: 29.



num = 600851475143
lpf = largetPrimeFactor(num)
print(format % (num, lpf))

# Largest prime factor of 600851475143! is: 6857.
