#!/bin/python3

import math
import os
import random
import re
import sys

'''
Example arr = [1,1,3,2,1]
i    arr[i]    result
0    1    [0, 1, 0, 0]
1    1    [0, 2, 0, 0]
2    3    [0, 2, 0, 1]
3    2   

# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''

def countingSort(arr):
    # Write your code here
    l = [0] * 100
    for i in arr:
        l[i] += 1
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
