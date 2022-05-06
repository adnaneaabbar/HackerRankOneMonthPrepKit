#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
10

Sample Output
4

(n + x) = (n ^ x) + 2*(n & x)

# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
'''

def sumXor(n):
    # Write your code here
    count = 0
    while n:
        if not n&1:
            count += 1
        n >>= 1
    return 2**count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
