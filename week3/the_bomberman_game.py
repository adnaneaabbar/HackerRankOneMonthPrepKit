#!/bin/python3

import math
import os
import random
import re
import sys

'''
Implementation of the third case is inspired by :
https://www.hackerrank.com/challenges/bomber-man/forum/comments/557085

Sample Input
STDIN           Function
-----           --------
6 7 3           r = 6, c = 7, n = 3
.......         grid =['.......', '...O...', '....O..',\
...O...                '.......', 'OO.....', 'OO.....']
....O..
.......
OO.....
OO.....

Sample Output
OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO

# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
'''

def bomberMan(n, grid):
    # Write your code here
    if n == 1:
        return grid
    
    r = len(grid)
    c = len(grid[0])
    if not n&1:
        return ['O'*c for j in range(r)]
    
    #replace symbols
    grid = [x.replace('O', '2') for x in grid]
    grid = [x.replace('.', '0') for x in grid]
    #split rows into list
    grid = [list(map(int, list(x))) for x in grid]
    
    t = 1
    while t < 4 + n % 4:
        t += 1
        #each second check whole grid
        destroyed = [] #for location of cells that will explode
        for i in range(r):
            for j in range(c):
                #decrease bomb timer (simultaneously with either planting or explosion)
                if grid[i][j] > 0:
                    grid[i][j] -= 1
                #plant
                if t % 2 == 0 and grid[i][j] == 0:
                    grid[i][j] = 3
                #explode
                elif grid[i][j] == 0:
                    destroyed.append([i, j])
                    if i < r-1: destroyed.append([i+1, j])
                    if i > 0: destroyed.append([i-1, j])
                    if j < c-1: destroyed.append([i, j+1])
                    if j > 0: destroyed.append([i, j-1])
        if destroyed:
            grid = [[2] * len(x) for x in grid]
            for i, j in destroyed:
                grid[i][j] = 0

    #convert lists to strings
    grid = [''.join(list(map(str, x))) for x in grid]
    #replace symbols
    grid = [x.replace('2', 'O') for x in grid]
    grid = [x.replace('0', '.') for x in grid]
    return grid
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
