def check(color):
    global cnt
    if not visited[i][j] and arr[i][j] == color:
        q.append([i, j])
        visited[i][j] = 1
        while q:
            x, y = q.pop(0)
            for k in range(4):
                ni = x + di[k]
                nj = y + dj[k]
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == color:
                    visited[ni][nj] = 1
                    q.append([ni, nj])
        cnt += 1

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
q = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

ans1 = 0
ans2 = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        check('R')
        check('B')
        check('G')
        ans1 += cnt

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        cnt = 0
        if not visited[i][j] and (arr[i][j] == 'R' or arr[i][j] == 'G'):
            q.append([i, j])
            visited[i][j] = 1
            while q:
                x, y = q.pop(0)
                for k in range(4):
                    ni = x + di[k]
                    nj = y + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and (arr[ni][nj] == 'R' or arr[ni][nj] == 'G'):
                        visited[ni][nj] = 1
                        q.append([ni, nj])
            cnt += 1
        check('B')
        ans2 += cnt

print(ans1, ans2)
