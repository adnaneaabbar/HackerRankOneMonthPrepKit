#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
11
middle-Outz
2

Sample Output
okffng-Qwvb

# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
'''

def caesarCipher(s, k):
    res = ""
    k %= 26
    # Write your code here
    for i in list(s):
        if (ord('A') <= ord(i) <= ord('Z') and ord('A') <= ord(i) + k <= ord('Z')) or (ord('a') <= ord(i) <= ord('z') and ord('a') <= ord(i) + k <= ord('z')):
            res += chr(ord(i) + k)
            continue
        if (ord('A') <= ord(i) <= ord('Z') and ord('Z') <= ord(i) + k):
            res += chr(ord('A') + ord(i) + k - ord('Z') - 1)
            continue
        if (ord('a') <= ord(i) <= ord('z') and ord('z') <= ord(i) + k):
            res += chr(ord('a') + ord(i) + k - ord('z') - 1)
            continue
        res += i
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
