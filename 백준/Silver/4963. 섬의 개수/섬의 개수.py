while True:
    w, h = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    q = []
    count = 0

    if w == 0 and h == 0:
        break

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                q.append([i, j])
                count += 1
                while q:
                    x, y = q.pop(0)
                    for k in range(8):
                        ni = x + di[k]
                        nj = y + dj[k]
                        if 0 <= ni < h and 0 <= nj < w and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            q.append([ni, nj])
    print(count)
