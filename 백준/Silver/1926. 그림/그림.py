n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
q = []

ans = 0
max_v = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] and not visited[i][j]:
            q.append([i, j])
            visited[i][j] = 1
            S = 1  # 가장 넓은 그림의 넓이를 위한 최솟값 설정
            while q:
                x, y = q.pop(0)
                for k in range(4):
                    ni = x + di[k]
                    nj = y + dj[k]
                    if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and paper[ni][nj]:
                        visited[ni][nj] = 1
                        q.append([ni, nj])
                        S += 1
            ans += 1
            max_v = max(max_v, S)

print(ans)
print(max_v)