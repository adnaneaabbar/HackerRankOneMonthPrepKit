#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
5 1
3 4 7 6 5

Sample Output
4
6
3
7
5

# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
'''

def SieveOfEratosthenes(n) :
    lower = 2
    upper = 10000
    return [i for i in range(lower, upper + 1) if all(i % j != 0 for j in range(2, i))]
        
def waiter(number, q):
    # Write your code here
    primes = SieveOfEratosthenes(10000)
    ans = []
    a = []
    b = []
    
    # iterations
    for i in range(q):
        # transfer to Ai or Bi depending on i'th prime
        while(number):
            topStack = number.pop()
            if topStack % primes[i] == 0:
                b.append(topStack)
            else:
                a.append(topStack)
        # transfer Bi to ans, top to bottom
        while(b):
            e = b.pop()
            ans.append(e)
        # update with new Ai
        number = a
        a = []
    # remaining values in Ai
    while(number):
        ans.append(number.pop())
    return(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
