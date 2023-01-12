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
4       t = 4
2 2     n = 2, m = 2
3 2     n = 3, m = 2
2 3     n = 2, m = 3
4 4     n = 4, m = 4

Sample Output
3  
7  
9  
3375

# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
'''

'''
http://oeis.org/A000078 for further reading abt tetranacci numbers
spent some days thinking about this problem, settled with the solution on the forum in the end
'''
def tetranacci(n): 
    arr = [1, 2, 4, 8]
    if n <= 4: 
        return arr[:n]
    else: 
        for i in range(4, n):
            arr.append(sum(arr[i-4:i])%(10**9 + 7))
    return arr

def legoBlocks(n, m):
    MOD = (10**9 +7)
    a, s = [pow(v, n, MOD) for v in tetranacci(m)], [1]

    for i in range(1, len(a)):
        sums = sum([x*y for x,y in zip(a[:i], s[::-1])])
        s.append( (a[i]-sums)%MOD)
    return s[-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
