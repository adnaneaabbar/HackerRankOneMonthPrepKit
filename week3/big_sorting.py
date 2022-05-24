#!/bin/python3

import math
import os
import random
import re
import sys


'''
Sample Input
6
31415962648954945654545454
1
3
10
3
5

Sample Output
1
3
3
5
10
31415962648954945654545454
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#
'''

def bigSorting(unsorted):
    # Write your code here
    return sorted(unsorted, key=lambda x : (len(x),x))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
