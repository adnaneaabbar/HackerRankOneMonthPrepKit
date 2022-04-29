#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
We promptly judged antique ivory buckles for the next prize

Sample Output
pangram

Sample Explanation
All of the letters of the alphabet are present in the string.

# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
'''

def pangrams(s):
    # Write your code here
    s = s.replace(" ", "").lower()
    alphabet = set(s)
    return "pangram" if len(alphabet) == 26 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
