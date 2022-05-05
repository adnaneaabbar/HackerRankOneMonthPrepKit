#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
2
3
1 2 3
4
1 2 3 3

Sample Output
NO
YES

# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''

def balancedSums(arr):
    # Write your code here
    total = sum(arr)
    left_sum = 0
    for a in arr:
        if left_sum * 2 == total - a:
            return "YES"
        left_sum += a
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
