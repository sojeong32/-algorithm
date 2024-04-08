from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
q = deque()
day = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i, j, day])
            visited[i][j] = 1  # 방문 표시
            # arr[i][j] = 1  # 토마토가 익는다.

while q:
    x, y, day = q.popleft()
    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
            arr[ni][nj] = arr[x][y] + 1  # 토마토가 익는 데 전 토마토보다 +1한 값 재할당
            visited[ni][nj] = 1
            q.append([ni, nj, day+1])

for i in arr:
    if 0 in i:
        print(-1)
        break

else:
    print(day)  # 맨 처음 익는데 걸린 시간을 1로 설정해놔서 출력은 1을 뺀 값으로 한다.
