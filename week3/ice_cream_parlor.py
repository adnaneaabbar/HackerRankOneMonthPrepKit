#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]

Sample Output
1 4
1 2

# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#
'''

def icecreamParlor(m, arr):
    # Write your code here
    idx = {}
    for i in range(len(arr)):
        if m - arr[i] in idx:
            return [idx[m - arr[i]], i + 1]
        idx[arr[i]] = i + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)
        print(result)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
