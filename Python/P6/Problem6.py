"""
Problem 6
Title:    Sum Square Difference
Author:   Paul Kim
Date:     6/19/2017

Description:
The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def sumOfSquares(N):
    sum = 0
    for i in range(1, N+1):
        sum += i*i
    return sum

def squareOfSums(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
    return sum*sum

format = """The difference betwen the sum of the square and the the square of
format the sum of all whole numbers in the range of 1 to %d is: %d"""

N = 10
sumSquareDiff = abs( squareOfSums(N) - sumOfSquares(N))
print(format % (N, sumSquareDiff))
# The difference betwen the sum of the square and the the square of
# format the sum of all whole numbers in the range of 1 to 10 is: 2640


N = 100
sumSquareDiff = abs( squareOfSums(N) - sumOfSquares(N))
print(format % (N, sumSquareDiff))
# The difference betwen the sum of the square and the the square of
# format the sum of all whole numbers in the range of 1 to 100 is: 25164150
