#!/bin/python3

import math
import os
import random
import re
import sys


#
'''
Sample Input
3
1 5
10 3
3 4

Sample Output
1

# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#
'''

def truckTour(petrolpumps):
    # Write your code here
    for i in range(len(petrolpumps)):
        tank = 0
        j = i + 1
        while j != i:
            tank += (petrolpumps[j - 1][0] - petrolpumps[j - 1][1])
            if tank < 0:
                break
            j += 1
            if j == len(petrolpumps):
                j = 0
        if tank < 0:
            continue
        else:
            return i
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
