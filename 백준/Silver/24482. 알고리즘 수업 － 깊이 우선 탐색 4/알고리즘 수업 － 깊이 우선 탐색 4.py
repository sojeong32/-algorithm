import sys
sys.setrecursionlimit(10 ** 6)

def dfs(cur, dep):
    visited[cur] = dep
    for w in adjl[cur]:
        if visited[w] == -1:
            dfs(w, dep+1)


N, M, R = map(int, sys.stdin.readline().split())
arr = [map(int, sys.stdin.readline().split()) for _ in range(M)]
adjl = [[] for _ in range(N+1)]
for u, v in arr:
    adjl[u].append(v)
    adjl[v].append(u)
visited = [-1] * (N+1)
for i in range(len(adjl)):
    adjl[i].sort(reverse=True)


dfs(R, 0)
for i in range(1, N+1):
    print(visited[i])