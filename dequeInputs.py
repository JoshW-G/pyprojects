# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
def append(arg):
    d.append(arg)
def appendleft(arg):
    d.appendleft(arg)
def pop():
    d.pop()
def popleft():
    d.popleft()

d = deque()
n = int(input())
cmnd = {"append" : append,
        "appendleft" : appendleft,
        "pop": pop,
        "popleft": popleft
    
}
for i in range(n):
    c = str(input()).split()
    if(c[0] in cmnd):
        if(len(c)>1):
            cmnd[c[0]](c[1])
        else:
            cmnd[c[0]]()
l = list(d)
for j in l:
    print(j, end=" ", flush=True)   
