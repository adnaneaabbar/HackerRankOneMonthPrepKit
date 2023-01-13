'''
Sample Input
STDIN       Function
-----       --------
5           Q = 5
1 4         insert 4
1 9         insert 9
3           print minimum
2 4         delete 4
3           print minimum

Sample Output
4  
9 
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import inf
q = int(input())
l = set()
minn = inf
for _ in range(q):
    line = input().strip().split()
    if len(line) == 1:
        print(minn)
    else:
        i, v = int(line[0]), int(line[1])
        if i == 1:
            if v < minn and len(l) != 0:
                minn = v
            l.add(v)
            if len(l) == 1:
                minn = v
        if i == 2:
            l.remove(v)
            if v == minn and len(l) != 0:
                minn = min(l)