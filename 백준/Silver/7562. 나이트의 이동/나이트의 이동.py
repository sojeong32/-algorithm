T = int(input())

di = [-1, -2, -2, -1, 1, 2, 2, 1]
dj = [-2, -1, 1, 2, 2, 1, -1, -2]

for t in range(T):
    l = int(input())
    cur = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    visited = [[-1]*l for _ in range(l)]

    q = [[cur[0], cur[1]]]
    visited[cur[0]][cur[1]] += 1
    while q:
        x, y = q.pop(0)
        if x == goal[0] and y == goal[1]:
            break
        for k in range(8):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < l and 0 <= nj < l and visited[ni][nj] == -1:
                visited[ni][nj] = visited[x][y] + 1
                q.append([ni, nj])
    print(visited[goal[0]][goal[1]])