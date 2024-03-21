def dfs(x):
    global check
    for w in adjl[x]:
        if w == k:
            check = True
            return
        if visited[w] == 1:
            continue
        visited[w] = 1
        result.append(x)
        dfs(w)


N = int(input())
adjl = [[] for _ in range(N+1)]
for j in range(1, N+1):
    adjl[j].append(int(input()))

ans = []


for k in range(1, N+1):
    if k == adjl[k][0]:
        ans.append(k)

for k in range(1, N+1):
    visited = [0]*(N+1)
    check = False
    result = []
    dfs(k)
    if check:
        ans.extend(result)

ans = list(set(ans))
ans.sort()
print(len(ans))
for z in ans:
    print(z)
