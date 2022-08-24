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
5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4  
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]

Sample Output
6

# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
'''

def equalStacks(h1, h2, h3):
    # Write your code here
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)
    i, j, k = 0, 0, 0
    while h1 and h2 and h3:
        m = max(s1, s2, s3)
        if(s1 == s2 == s3):
            return s1
        if(m == s1):
            s1 = s1 - h1[i]
            i += 1
        if(m == s2):
            s2 = s2 - h2[j]
            j += 1
        if(m == s3):
            s3 = s3 - h3[k]
            k += 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
