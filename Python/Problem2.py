# Each new term in the Fibonacci sequence is generate by adding the previous two
# two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

# Test method for Recursive Fibonacci
def re_Fib( i ):
    if i == 0:
        return 1
    elif i == 1:
        return 2
    return re_Fib( i-1 ) + re_Fib( i-2 )

# Test method for even Fibonacci below a given upperBound
def even_Fib_Sum_Bounded( upperBound ):
    sum = 0
    for i in range(upperBound):
        x = re_Fib(i)
        # if the ith Fibonacci value is even:
        if (x & 1) == 0:
            sum += x
    return sum

# Actual method for finding summation of Fibonacci values below 4 million
def even_Fib_Sum():
    sum = 0
    i = 0
    fibVal = 0
    while fibVal < 4000000:
        fibVal = re_Fib(i)
        if (fibVal & 1) == 0:
            sum += fibVal
        i += 1
    return sum

upperBound = 10
format = "Sum of all even Fibonacci values below %d is: %d."

# sum = even_Fib_Sum_Bounded(upperBound)
# print(format % (upperBound, sum))

sum = even_Fib_Sum()
print(format % (upperBound, sum))
# Sum of all even Fibonacci values below 10 is: 4613732.
