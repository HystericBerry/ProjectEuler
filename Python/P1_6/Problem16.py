"""
Problem 16
Title:    Power Digit Sum
Author:   Paul Kim
Date:     6/20/2017

Description:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sumDigits(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum

def Main():
    format = "The sum of the digits of the number 2^%d is: %d"

    N = 15
    digits = str(2**N)
    sumOfDigits = sumDigits(digits)
    print(format % (N, sumOfDigits))
    # The sum of the digits of the number 2^15 is: 26

    N = 1000
    digits = str(2**N)
    sumOfDigits = sumDigits(digits)
    print(format % (N, sumOfDigits))
    # The sum of the digits of the number 2^1000 is: 1366

Main()
