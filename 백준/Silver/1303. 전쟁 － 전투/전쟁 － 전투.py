N, M = map(int, input().split())
soldiers = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
q = []
total_w = 0
total_b = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0 and soldiers[i][j] == 'W':
            q.append([i, j])
            visited[i][j] = 1
            count_w = 1
            while q:
                y, x = q.pop(0)
                for k in range(4):
                    nj = x + dj[k]
                    ni = y + di[k]
                    if 0 <= ni < M and 0 <= nj < N and soldiers[ni][nj] == 'W' and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        q.append([ni, nj])
                        count_w += 1
            total_w += count_w ** 2

        if visited[i][j] == 0 and soldiers[i][j] == 'B':
            q.append([i, j])
            visited[i][j] = 1
            count_b = 1
            while q:
                y, x = q.pop(0)
                for k in range(4):
                    nj = x + dj[k]
                    ni = y + di[k]
                    if 0 <= ni < M and 0 <= nj < N and soldiers[ni][nj] == 'B' and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        q.append([ni, nj])
                        count_b += 1
            total_b += count_b ** 2
print(total_w, total_b)
