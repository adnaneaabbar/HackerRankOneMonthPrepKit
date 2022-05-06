#!/bin/python3

import math
import os
import random
import re
import sys



'''
Sample Input
2 3
2 4
16 32 96

Sample Output
3

# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
'''

def getTotalX(a, b):
    # Write your code here
    left = max(a)
    right = min(b)
    count = 0
    for i in range(left, right + 1):
        if a_factors(a, i) and b_factors(b, i):
            count += 1
    return count
        
def a_factors(a, val):
    for e in a:
        if not val%e:
            continue
        else:
            return False
    return True

def b_factors(b, val):
    for e in b:
        if not e%val:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
