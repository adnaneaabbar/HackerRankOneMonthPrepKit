'''
Sample Input
STDIN   Function
-----   --------
8       Q = 8
1 abc   ops[0] = '1 abc'
3 3     ops[1] = '3 3'
2 3     ...
1 xy
3 2
4 
4 
3 1

Sample Output
c
y
a
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
ops = []
for i in range(q):
    inp = input().split(' ')
    ops.append(inp)

s = []
memory = []
for op in ops:
    if op[0] == '1':
        app = op[1]
        memory.append(s.copy())
        s.extend(app)
    elif op[0] == '2':
        k = int(op[1])
        memory.append(s.copy())
        del s[-k:]
    elif op[0] == '3':
        k = int(op[1])
        print(s[k - 1])
    else:
        s = memory.pop()