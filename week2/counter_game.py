#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
1
6

Sample Output
Richard

# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
'''

def counterGame(n):
    # Write your code here
    # n - 1 flips trailing zeros to ones therefore we can only count ones to know number of rounds
    # if even Richard wins, else Louise because she starts
    return "Louise" if (bin(n-1)[2:].count('1'))&1 else "Richard"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()