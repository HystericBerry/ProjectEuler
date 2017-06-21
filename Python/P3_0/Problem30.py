"""
Problem 30
Title:    Digit Fifth Powers
Author:   Paul Kim
Date:     6/20/2017

Description:
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    1634 = 1^4 + 6^4 + 3^4 + 4^4
As 1 = 1^4 is not a sum, it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

def sumDigits(cache, N, p):
    sum = 0
    n = N
    while n != 0:
        i = int(n % 10)
        sum += cache[i]
        n /= 10
    return sum

def Main():
    format = "The sum of all numbers of fifth power digits is: %d"
    N = 500000
    p = 5
    cache = [x**p for x in list(range(10))]

    sum = 0
    for i in range(10, N):
        n = sumDigits(cache, i, p)
        if i == n:
            sum += n
    print(format % (sum))
    # The sum of all numbers of fifth power digits is: 443839
    
Main()
