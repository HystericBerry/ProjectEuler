"""
Problem 5
Title:    Smallest Multiple
Author:   Paul Kim
Date:     6/19/2017

Description:
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
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

# returns a map of <K = factor, V = num factor occurence> where the map
# represents all factors of the given number N
def smallestMultiple(N):
    smallestMult = {}
    for i in range(2, N+1):
        factors = minFactor(i)

        for K, V in factors.items():
            occur = smallestMult.get(K)
            if occur == None or V > occur:
                # update factor entry
                smallestMult[K] = V

    smallestProduct = 1
    for K, V in smallestMult.items():
        smallestProduct = smallestProduct * (K**V)
    return smallestProduct

# returns a map of all factors and number of occurence of each factor
# this does not include 1
def minFactor(N):
    cache = {}
    max = int(math.ceil(math.sqrt(N)))+1
    primeFactors = primeSieve(max)
    for i in reversed(primeFactors):
        count = 0
        # while N is divisible by i
        while N % i == 0:
            N = N/i
            count += 1
        if count != 0:
            cache[i] = count

    if N != 1:
        cache[N] = 1

    return cache


#####MAIN METHOD#####
format = "The smallest positive number evenly divisible by all numbers between "
format += "1 and %d is: %d."

N = 10
factors = smallestMultiple(N)
print(format % (N, factors))

# The smallest positive number evenly divisible by all numbers between 1 and
# 10 is: 2520.

N = 20
factors = smallestMultiple(N)
print(format % (N, factors))

# The smallest positive number evenly divisible by all numbers between 1 and 20
# is: 232792560.
