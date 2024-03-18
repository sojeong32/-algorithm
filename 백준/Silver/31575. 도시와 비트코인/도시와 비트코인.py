def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1

    while q:
        a, b = q.pop(0)
        if a == m - 1 and b == n - 1:
            return 'Yes'

        for k in range(2):
            ni = a + di[k]
            nj = b + dj[k]

            if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj])
    return 'No'


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
di = [0, 1]  # 우,하 방향설정
dj = [1, 0]
q = []

print(bfs(0, 0))
