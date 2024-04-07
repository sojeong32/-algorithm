# 쉬운 최단거리

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
depth = 0
q = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append([i, j])
            visited[i][j] = 1
            arr[i][j] = 0
while q:
    x, y = q.pop(0)
    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
            q.append([ni, nj])
            visited[ni][nj] = 1
            arr[ni][nj] = arr[x][y] + 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            arr[i][j] = -1

for i in arr:
    print(*i)