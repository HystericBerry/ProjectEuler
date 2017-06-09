# Problem 20
# Title:    Even Fibonacci numbers
# Author:   Paul Kim
# Date:     6/9/2017

# Description:
# n! means n * (n-1) * ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the
# digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

def factorial( n ):
    fact = 1;
    for i in range(1, n+1):
        fact = fact * i
    return fact

def sum_of_elements( n ):
    stringVal = str(n)
    sum = 0
    for c in stringVal:
        sum += int(c)
    return sum



#####MAIN METHOD#####
format = "Sum of all digits of %d! is: %d."
n = 100
fact = factorial(n)

sum = sum_of_elements(fact)
print(format % (n, sum))
