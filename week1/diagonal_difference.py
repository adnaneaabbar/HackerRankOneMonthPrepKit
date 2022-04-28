#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
3
11 2 4
4 5 6
10 8 -12

Sample Output
15

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
'''

def diagonalDifference(arr):
    # Write your code here
    n = len(arr[0])
    return abs(sum(arr[i][i] for i in range(n)) - sum(arr[i][n-i-1] for i in range(n)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
