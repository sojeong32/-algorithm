# 미로탐색
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)] # arr와 같은 빈 행렬 만들기
# print(arr)
di = [0, 1, 0, -1] #우, 하, 좌, 상 방향설정
dj = [1, 0, -1, 0]

def maze(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            new_i = x + di[k]
            new_j = y + dj[k]

            if 0 <= new_i < N and 0 <= new_j < M:
                if arr[new_i][new_j] == 1 and visited[new_i][new_j] == 0:
                    visited[new_i][new_j] = visited[x][y] + 1
                    q.append((new_i, new_j))

                if new_i == N-1 and new_j == M-1:
                    return visited[new_i][new_j]

print(maze(0,0))