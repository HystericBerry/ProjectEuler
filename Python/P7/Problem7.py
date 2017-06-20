"""
Problem 7
Title:    10001st prime
Author:   Paul Kim
Date:     6/19/2017

Description:
By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see that the
6th prime is 13.

What is the 10001st prime number?
"""

# returns a list of primes less than N (exclusive)
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

#####MAIN METHOD#####
def Main():
    format = "The %dth prime number is: %d"
    N = 10001
    primes = primeSieve(105000)

    print("The first 6 prime numbers: ", primes[:6])
    print(format % (N, primes[N-1]))
    # The 10001th prime number is: 104743

Main()
