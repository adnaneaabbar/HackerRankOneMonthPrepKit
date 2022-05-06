#!/bin/python3

import math
import os
import random
import re
import sys

'''
Example:
n = '9875'
k = 4

superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
superDigit(p) = superDigit(116)
                  1+1+6 = 8
superDigit(p) = superDigit(8)

Sample Output
8

# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
'''

def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return int(n)
    return superDigit(str(sum(map(int, n)) * k), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
