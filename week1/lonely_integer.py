#!/bin/python3

import math
import os
import random
import re
import sys

'''
Example a = [1,2,3,4,3,2,1]
The unique element is 4

# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
'''

def lonelyinteger(a):
    # Write your code here
    for i in a:
        if a.count(i) == 1:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
