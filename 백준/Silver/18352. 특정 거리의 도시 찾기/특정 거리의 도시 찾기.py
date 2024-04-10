import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    adjl[i].append(j)

q = deque()
q.append(x)
visited[x] = 1
ans = []
while q:
    x = q.popleft()
    if visited[x] > k+1:
        break

    for w in adjl[x]:
        if visited[w] == 0:
            visited[w] = visited[x] + 1
            q.append(w)
            if visited[w] == k+1:
                ans.append(w)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for k in ans:
        print(k)