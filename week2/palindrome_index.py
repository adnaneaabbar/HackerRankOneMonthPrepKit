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
3       q = 3
aaab    s = 'aaab' (first query)
baa     s = 'baa'  (second query)
aaa     s = 'aaa'  (third query)

Sample Output
3
0
-1

# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
'''

def palindromeIndex(s):
    # Write your code here
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            pal_test = s[:i] + s[i+1:]
            if pal_test == pal_test[::-1]:
                return i
            return len(s) - 1 - i
    return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
