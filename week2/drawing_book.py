#!/bin/python3

import math
import os
import random
import re
import sys

'''
Example:
n = 5, p = 3

Outpuut:
1

# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#
'''

def pageCount(n, p):
    # Write your code here
    return min(get_position(n) - get_position(p), get_position(p) - 1)

def get_position(x):
    return (x + 1) // 2 if x&1 else (x // 2) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
