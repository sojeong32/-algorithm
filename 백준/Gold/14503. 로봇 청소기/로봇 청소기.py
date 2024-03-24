from collections import deque

N, M = map(int, input().split())
si, sj, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# print(arr)
di = [-1, 0, 1, 0]  # 상,우,하,좌 방향설정
dj = [0, 1, 0, -1]

q = deque()
q.append([si, sj, direction])
arr[si][sj] = 2  # 벽 1과 구분하기 위해 청소한 곳은 2로 설정
visited[si][sj] = 2
count = 1
while q:
    i, j, dir = q.popleft()
    for k in range(4):  # 반시계방향으로 둘러보며 청소되지 않은 빈 칸 청소하기
        new_dir = (dir - k + 3) % 4
        ni = i + di[new_dir]
        nj = j + dj[new_dir]

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 2  # 청소한다.
            arr[ni][nj] = 2
            count += 1
            q.append([ni, nj, new_dir])
            break

    else:  # 반시계방향으로 둘러보며 청소되지 않은 빈칸이 없다면
        ni = i - di[dir]
        nj = j - dj[dir]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
            if not visited[ni][nj]:  # 방문을 안한 곳이면
                visited[ni][nj] = 2  # 청소한다.
                arr[ni][nj] = 2
                count += 1
            q.append([ni, nj, dir])  # 방문(청소)를 했든 안했든 그 위치로 간다.


print(count)