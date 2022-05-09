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
2           t = 2
5           n = 5
2 1 5 3 4   q = [2, 1, 5, 3, 4]
5           n = 5
2 5 1 3 4   q = [2, 5, 1, 3, 4]

Sample Output
3
Too chaotic

# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
'''

def minimumBribes(q):
    # Write your code here
    q = [i - 1 for i in q]
    res = 0
    for idx, person in enumerate(q):
        if person - idx > 2:
            print("Too chaotic")
            return
        for j in q[max(person - 1, 0): idx]:
            if j > person:
                res += 1
    print(res)            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
