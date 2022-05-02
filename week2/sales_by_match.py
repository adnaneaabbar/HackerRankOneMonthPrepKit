#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

Sample Output
3

# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
'''

def sockMerchant(n, arr):
    # Write your code here
    freq = [0] * 101
    for i in range(n):
        freq[arr[i]] += 1
    return sum(i//2 for i in freq)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
