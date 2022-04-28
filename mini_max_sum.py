#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
1 2 3 4 5

Sample Output
10 14

# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    print(sum(arr[:4]), sum(arr[1:]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
