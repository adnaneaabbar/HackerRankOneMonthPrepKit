#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
2 
4 
1 2 3 4
6
2 -1 2 3 4 -5

Sample Output
10 10
10 11

# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
'''

def maxSubarray(arr):
    # Write your code here
    i = j = k = arr[0]
    for index, val in enumerate(arr):
        if index == 0:
            continue
        k = max(k, val, k + val)
        i = max(val, val + i)
        j = max(j, i)
    return [j, k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
