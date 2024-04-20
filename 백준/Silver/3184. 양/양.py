r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
q = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

total_lamb = 0
total_wolf = 0
for i in range(1, r-1):
    for j in range(1, c-1):
        if (arr[i][j] == 'v' or arr[i][j] == 'o') and visited[i][j] == 0:
            lamb_cnt = 0
            wolf_cnt = 0
            if arr[i][j] == 'v':
                wolf_cnt = 1
            else:
                lamb_cnt = 1
            visited[i][j] = 1
            q.append([i, j])

            while q:
                x, y = q.pop(0)
                for k in range(4):
                    ni = x + di[k]
                    nj = y + dj[k]
                    if 1 <= ni < r-1 and 1 <= nj < c-1 and (arr[ni][nj] == 'v' or arr[ni][nj] == '.') and visited[ni][nj] == 0:
                        if arr[ni][nj] == 'v':
                            wolf_cnt += 1
                        visited[ni][nj] = 1
                        q.append([ni, nj])
                    if 1 <= ni < r-1 and 1 <= nj < c-1 and (arr[ni][nj] == 'o' or arr[ni][nj] == '.') and visited[ni][nj] == 0:
                        if arr[ni][nj] == 'o':
                            lamb_cnt += 1
                        visited[ni][nj] = 1
                        q.append([ni, nj])

            if lamb_cnt > wolf_cnt:
                total_lamb += lamb_cnt
            else:
                total_wolf += wolf_cnt

print(total_lamb, total_wolf)