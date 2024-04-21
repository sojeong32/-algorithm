import sys
sys.setrecursionlimit(10**6)

def dfs(s):
    global order
    visited[s] = order
    for w in adjl[s]:
        if visited[w] != 0:
            continue
        order += 1
        visited[w] = order
        dfs(w)

n, m, r = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    adjl[i].append(j)
    adjl[j].append(i)

for l in adjl:
    l.sort()

order = 1
dfs(r)
for k in range(1, n+1):
    print(visited[k])