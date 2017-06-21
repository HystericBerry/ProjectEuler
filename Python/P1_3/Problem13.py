"""
Problem 13
Title:    Large Sum
Author:   Paul Kim
Date:     6/20/2017

Description:
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.

37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
...
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690
"""

import sys, os

def Main():
    format = "The first %d digits of the large sum is: %s"
    path = os.path.join(os.path.dirname(__file__), "input.in")
    f = open(path)

    sum = 0
    for s in f:
        sum += int(s[:11])

    N = 10
    tenDigitSum = str(sum)[0:N]

    print(format % (N, tenDigitSum))
    f.close()

    # The first 10 digits of the large sum is: 5537376230

Main()
