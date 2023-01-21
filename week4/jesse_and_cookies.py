#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
STDIN               Function
-----               --------
6 7                 A[] size n = 6, k = 7
1 2 3 9 10 12       A = [1, 2, 3, 9, 10, 12]  

Sample Output
2

# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
'''

# priority queue
import heapq

def cookies(k, A):
    heapq.heapify(A)
    ans = 0
    while A[0] < k:
        if len(A) == 1:
            return -1
        least = heapq.heappop(A)
        s_least = heapq.heappop(A)
        heapq.heappush(A, least + 2 * s_least)
        ans += 1
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
