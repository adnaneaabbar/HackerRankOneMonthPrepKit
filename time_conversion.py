#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
07:05:45PM

Sample Output
19:05:45

# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
'''
def timeConversion(s):
    s = list(s)
    # Write your code here
    if s[-2] == 'P':
        if int(str(s[0] + s[1])) < 12:
            newHour = str(int(str(s[0] + s[1])) + 12)
            s[0] = newHour[0]
            s[1] = newHour[1]
        return "".join(s[-len(s):-2])
    else:
        if int(str(s[0] + s[1])) >= 12:
            newHour = '0' + str(int(str(s[0] + s[1])) - 12)
            s[0] = newHour[0]
            s[1] = newHour[1]
        return "".join(s[-len(s):-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
