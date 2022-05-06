#!/bin/python3

import math
import os
import random
import re
import sys



'''
Sample Input 
6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx

Sample Output
3
1
-1
2
0
1

https://docs.python.org/3/library/collections.html#counter-objects

# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
'''

from collections import Counter

def anagram(s):
    # Write your code here
    n = len(s)
    if n&1:
        return -1
    left = Counter(s[:n//2])
    right = Counter(s[n//2:])
    diff = right - left
    
    return sum(diff.values())
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
