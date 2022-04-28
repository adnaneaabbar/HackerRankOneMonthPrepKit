#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
3 
2147483647 
1 
0

Sample Output
2147483648 
4294967294 
4294967295

# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
'''

def flippingBits(n):
    # Write your code here
    return (2**32 - 1) - n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
