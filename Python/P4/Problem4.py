"""
Problem 4
Title:    Largest Prime Factor
Author:   Paul Kim
Date:     6/19/2017

Description:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 90 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalin(N):
    N = str(N)
    return isPalineHelper(N, 0, len(N)-1)

def isPalineHelper(N, start, end):
    if start >= end:
        return True

    return False if N[start] != N[end] else isPalineHelper(N, start+1, end-1)

def largestPalinProduct(N):
    products = set()
    for i in range(1, N):
        for j in range(1, N):
            products.add(i*j)

    products = list(products)
    products.sort()

    count = range(len(products))[::-1]
    for i in count:
        if isPalin(products[i]):
            return products[i]

    return -1

#####MAIN METHOD#####
def Main():
    format = "%d is the largest palindrome product!"
    N = 1000
    lpp = largestPalinProduct(N)
    print(format % (lpp))

    # 906609 is the largest palindrome product!

Main()
