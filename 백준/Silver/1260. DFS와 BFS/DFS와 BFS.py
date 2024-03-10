def dfs(x):
    visited1[x] = 1
    print(x, end=' ')
    for w in adjl[x]:
        if visited1[w] == 1:
            continue
        dfs(w)

def bfs(x):
    visited2[x] = 1
    print(x, end=' ')
    for w in adjl[x]:
        q.append(w)

    while q:
        x = q.pop(0)
        if visited2[x] == 1:
            continue
        bfs(x)


N, M, V = map(int, input().split())
adjl = [[] for _ in range(N+1)]
visited1 = [0]*(N+1)
visited2 = [0]*(N+1)
for _ in range(M):
    i, j = map(int, input().split())
    adjl[i].append(j)
    adjl[j].append(i)


for k in adjl:  # 정점번호가 작은 것부터 방문하려고 정렬
    k.sort()

q = []
dfs(V)
print()
bfs(V)
