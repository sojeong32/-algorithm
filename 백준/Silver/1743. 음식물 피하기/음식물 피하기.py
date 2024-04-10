n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

q = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
max_size = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:  # 방문하지 않은 음식물쓰레기 있는 곳
            q.append([i, j])  # 위치 저장
            visited[i][j] = 1  # 방문표시

            size = 1
            while q:
                x, y = q.pop(0)
                for k in range(4):
                    ni = x+di[k]
                    nj = y+dj[k]
                    if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        q.append([ni, nj])
                        visited[ni][nj] = 1
                        size += 1
            if max_size < size:
                max_size = size
print(max_size)