from collections import deque
from sys import stdin; input = stdin.readline
N = int(input())
cmd = []
# front = rear = -1
q = deque()
for n in range(N):
    cmd.append(input().split())
# print(cmd)
for i in cmd:
    if i[0] == 'push':
        q.append(i[1])
    elif i[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(q))
    elif i[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif i[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif i[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)