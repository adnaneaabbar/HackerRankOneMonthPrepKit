#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
aabbcd

Sample Output
NO

# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
'''

from collections import Counter

def isValid(s):
    # Write your code here
    s = Counter(s)
    s = Counter(s.values())
    if len(s.values()) == 1:
        return "YES"
    elif len(s.values()) == 2:
        key1, key2 = s.keys()
        if s[key1] == 1 and (key1 - 1 == key2 or key1 == 1):
            return "YES"
        elif s[key2] == 1 and (key2 - 1 == key1 or key2 == 1):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
