#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
7
100 100 50 40 40 20 10
4
5 25 50 120

Sample Output
6
4
2
1

# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
'''

from bisect import bisect_right
from collections import Counter

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked_s = list(set(ranked))
    res = []
    n = len(ranked_s)
    for p in player:
        while n > 0 and p >= ranked_s[n - 1]:
            n -= 1
        res.append(n + 1)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
