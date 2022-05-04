#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
STDIN   Function
-----   --------
1       t = 1
5       n = 5
ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
fghij
olmkn
trpqs
xywuv

Sample Output
YES

# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
'''

def gridChallenge(grid):
    # Write your code here
    grid = [list(row) for row in grid]
    n = len(grid[0])
    for row in grid:
        row.sort()
    for j in range(n):
        for i in range(n - 1):
            if grid[i][j] > grid[i+1][j]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
