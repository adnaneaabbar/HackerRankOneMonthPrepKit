#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample Output
0.500000
0.333333
0.166667

# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''

def plusMinus(arr):
    # Write your code here
    print(len(list(filter(lambda x: x > 0, arr))) / len(arr))
    print(len(list(filter(lambda x: x < 0, arr))) / len(arr))
    print(len(list(filter(lambda x: x == 0, arr))) / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
