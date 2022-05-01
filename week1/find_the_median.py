#!/bin/python3

import math
import os
import random
import re
import sys



'''
Sample Input:
7
0 1 2 4 6 5 3

Sample Output:
3

# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''

def findMedian(arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    if n % 2 != 0:
        return arr[n//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
