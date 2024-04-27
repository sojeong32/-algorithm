T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = []

    for k in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and field[i][j]:
                q.append([i, j])
                while q:
                    r, c = q.pop(0)
                    visited[r][c] = 1
                    for k in range(4):
                        ni = r + di[k]
                        nj = c + dj[k]
                        if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 1 and visited[ni][nj] == 0:
                            q.append([ni, nj])
                            visited[ni][nj] = 1

                count += 1
    print(count)





