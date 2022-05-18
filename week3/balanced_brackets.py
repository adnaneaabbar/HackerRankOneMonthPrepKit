#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
STDIN                   Function 
-----                   -------- 
3                       n = 3 
{[()]}                  first s = '{[()]}' 
{[(])}                  second s = '{[(])}' 
{{[[(())]]}}            third s ='{{[[(())]]}}'

Sample Output
YES
NO
YES

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
'''

def isBalanced(s):
    # Write your code here
    stack = []
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    for c in s:
        if not stack or c not in brackets:
            stack.append(c)
        elif brackets[c] == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
            
    return "YES" if not stack else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
