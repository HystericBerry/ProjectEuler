# Problem 1
# Title:    Multiples of 3 or 5
# Author:   Paul Kim
# Date:     6/9/2017

# Description
# If we list all the natural numbers below 10 that are multiples of 3 OR 5, we
# get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

#####UNOPTIMIZED METHOD#####
# Modulo three or five multiple method
def three_five_mult( counter ):
    if counter % 3 == 0:
        return counter
    elif counter % 5 == 0:
        return counter
    else:
        return -1
# Summation method that utilizes three or five Modulo method
def three_five_mult_sum( max ):
    sum = 0
    for i in range(1,max):
        if not(three_five_mult(i) == -1):
            sum += i
    return sum
#####UNOPTIMIZED METHOD#####



#####OPTIMIZED METHOD#####
def three_five_mult_sumOpt( max ):
    sum = 0
    isThree = 0
    isFive = 0
    either = False
    for i in range(1, max):
        either = False
        isThree += 1
        isFive += 1
        if isThree == 3:
            either = True
            isThree = 0
        if isFive == 5:
            either = True
            isFive = 0

        if either:
            sum += i

    return sum
#####OPTIMIZED METHOD#####



#####MAIN METHOD#####
upperBound = 1000
format = "sum of all whole numbers below %d is: %d."

# unoptimized method call
# sum = three_five_mult_sum(upperBound)
# print(format % (upperBound, sum))

# optimized method call
sum = three_five_mult_sumOpt(upperBound)
print(format % (upperBound, sum))
# sum of all whole numbers below 1000 is: 233168.
