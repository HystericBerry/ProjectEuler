"""
Problem 8
Title:    Largest Product in a Series
Author:   Paul Kim
Date:     6/19/2017

Description:
The four adjacent digits in the 1000-digit number that have the greatest product
are 9 * 9 * 8 * 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. what is the value of this product?
"""
#####LIBRARIES#####
import sys, os

#####FUNCTIONS#####
# returns a map of <K = digit, V = num occurence of digit>. The map represents
# the number of digits in the given string but does not track position of digits.
def toDigits(s):
    digits = {}
    for c in s:
        i = int(c)
        if i in digits:
            digits[i] = digits.get(i)+1
        else:
            digits[i] = 1
    return digits

# returns the product of all digits represented by the Map
def digitsToProduct(digits):
    product = 1
    for K, V in digits.items():
        product *= (K**V)
    return product

# returns the curr N digits given an index, the prev string, curr string, and
# the starting position
def currString(N, curr, next, start):
    end = start + N
    if end < len(curr) or next == None:
        return curr[start:end]
    else:
        end = N - (len(curr) - start)
        return curr[start:] + next[:end]

def largestProductOfAdjacent(path, N):
    f = open(path)
    curr = f.readline()
    curr = curr.strip()

    digitString = None
    max = -sys.maxsize

    if curr != None:
        for next in f:
            next = next.strip()
            for i in range(len(curr)):
                s = currString(N, curr, next, i)
                digits = toDigits(s)
                product = digitsToProduct(digits)
                if product > max:
                    max = product
                    digitString = s
            curr = next

        next = None
        for i in range(len(curr)-N+1):
            s = currString(N, curr, next, i)
            digits = toDigits(s)
            product = digitsToProduct(digits)
            if product > max:
                max = product
                digitString = s
    f.close()
    return digitString, max


#####MAIN METHOD#####
def Main():
    format = "The largest product of %d adjacent digits is: %s = %d"
    path = os.path.join(os.path.dirname(__file__), "digits.in")

    N = 4
    digits, largest = largestProductOfAdjacent(path, N)
    print(format % (N, digits, largest))
    # The largest product of 4 adjacent digits is: 9989 = 5832

    N = 13
    digits, largest = largestProductOfAdjacent(path, N)
    print(format % (N, digits, largest))
    # The largest product of 13 adjacent digits is: 5576689664895 = 23514624000

Main()
