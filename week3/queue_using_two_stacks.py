'''
Sample Input
STDIN   Function
-----   --------
10      q = 10 (number of queries)
1 42    1st query, enqueue 42
2       dequeue front element
1 14    enqueue 42
3       print the front element
1 28    enqueue 28
3       print the front element
1 60    enqueue 60
1 78    enqueue 78
2       dequeue front element
2       dequeue front element

Sample Output
14
14
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
s1 = []
s2 = []
for t in range(int(input())):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        s2.append(q[1])
    
    elif q[0] == 2:
        if not s1:
            while s2:
                s1.append(s2.pop())
        s1.pop()
        
    else:
        print(s1[-1] if s1 else s2[0])