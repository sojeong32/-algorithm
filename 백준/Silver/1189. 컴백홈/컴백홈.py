def dfs(x, y):
    global ans, k

    if visited[x][y] > k:
        return

    if x == 0 and y == c-1:
        if visited[x][y] == k:
            ans += 1
        return

    for l in range(4):
        ni = x + di[l]
        nj = y + dj[l]
        if 0 <= ni < r and 0 <= nj < c and road[ni][nj] == '.' and not visited[ni][nj]:
            visited[ni][nj] = visited[x][y]+1
            dfs(ni, nj)
            visited[ni][nj] = 0

r, c, k = map(int, input().split())
road = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

visited[r-1][0] = 1
ans = 0

dfs(r-1, 0)
print(ans)