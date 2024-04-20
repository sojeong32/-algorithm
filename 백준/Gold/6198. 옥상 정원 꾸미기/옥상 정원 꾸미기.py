import sys
from collections import deque

N = int(input())
bd = deque()
for _ in range(N):
    bd.append(int(sys.stdin.readline()))

st = []
sumone = 0
while bd:
    if not st:
        st.append(bd.popleft())

    elif bd[0] < st[-1]:
        st.append(bd.popleft())
        sumone += len(st) - 1
    else:
        st.pop()


print(sumone)