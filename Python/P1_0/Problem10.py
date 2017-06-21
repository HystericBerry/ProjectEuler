"""
Problem 10
Title:    Summation of Primes
Author:   Paul Kim
Date:     6/20/2017

Description:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

def primeSieve(N):
    primes = [True]*(N+1)

    size = int(math.ceil(math.sqrt(N+1)))
    for i in range(2, size):
        if primes[i]:
            for j in range(2, N+1):
                if i*j >= N+1:
                    break
                primes[i*j] = False
    return primes

def primeListToSet(lst):
    primes = set()
    for i in range(2, len(lst)):
        if lst[i]:
            primes.add(i)
    return primes

def Main():
    format = "The sum of all primes below %d is: %d"

    N = 10
    lst = primeSieve(N-1)
    primes = primeListToSet(lst)
    del lst[:]
    total = sum(primes)
    print(format % (N, total))
    # The sum of all primes below 10 is: 17

    N = 2000000
    lst = primeSieve(N-1)
    primes = primeListToSet(lst)
    del lst[:]
    total = sum(primes)
    print(format % (N, total))
    # The sum of all primes below 2000000 is: 142913828922

Main()
