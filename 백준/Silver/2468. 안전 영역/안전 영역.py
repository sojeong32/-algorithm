# 안전 영역
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
for i in range(0, 101): # 비의 양이 정해지지 않았기에 0부터 건물 높이까지 1씩 증가하면서 계산
    q = deque()
    visited = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]  # 우,하,좌,상 방향 설정
    dj = [1, 0, -1, 0]

    # ans = 0
    count = 0  # 시작 때의 안전영역 수 0부터 시작
    for r in range(N):   # arr 탐색
        for c in range(N):
            # count = 0  # 시작 때의 안전영역 수 0부터 시작
            if arr[r][c] > i and visited[r][c] == 0:  # 비에 잠기지 않고 방문안한 곳부터 시작
                q.append((r, c))
                visited[r][c] = 1  # 시작점 방문표시

                while q: #큐에 값이 있으면 계속 돌아감
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + di[k]
                        ny = y + dj[k]
                        if 0 <= nx < N and 0 <= ny < N:  #이동하려는 곳의 범위가 NxN행렬 안에 있다면
                            if visited[nx][ny] == 1:  # 방문한 곳이면 넘어감
                                continue
                            elif arr[nx][ny] > i:  # 방문하지 않고 물에 잠기지 않았다면
                                visited[nx][ny] = 1  # 방문표시
                                q.append((nx, ny))

                count += 1  # 시작점에서 잠기지 않은 연결된 곳 다 탐색했으면 안전영역 수 1 증가
        
    if max_v < count:
        max_v = count


print(max_v)

