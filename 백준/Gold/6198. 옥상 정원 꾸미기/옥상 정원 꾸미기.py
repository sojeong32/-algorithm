import sys
from collections import deque

N = int(input())
bd = deque()
for _ in range(N):
    bd.append(int(sys.stdin.readline()))

st = []
sumone = 0
while bd:
    while True:
        if not st:
            if bd:
                st.append(bd.popleft())
                break
            else:
                break
        elif bd[0] < st[-1]:
            st.append(bd.popleft())
            sumone += len(st) - 1
            break
        else:
            st.pop()
            break

print(sumone)