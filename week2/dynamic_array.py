#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

Sample Output
7
3

# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
'''

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)]
    lastAnswer = 0
    ans = []
    for q in queries:
        x = q[1]
        y = q[2]
        if q[0] == 1:
            idx = ((x ^ lastAnswer) % n)
            arr[idx].append(y)
        else:
            idx = ((x ^ lastAnswer) % n)
            lastAnswer = arr[idx][y % len(arr[idx])]
            ans.append(lastAnswer)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
