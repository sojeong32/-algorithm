def bfs(x, y):
    global number
    global house_num
    q.append([x, y])
    visited[x][y] = 1
    house_num = 1

    while q:
        a, b = q.pop(0)
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                house_num += 1
                q.append([ni, nj])
    number += 1
    house_num_list.append(house_num)
    return


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
number = 0
house_num = 1
q = []
house_num_list = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)

print(number)
house_num_list.sort()  # 단지 내 집의 수 오름차순으로 정렬
for k in house_num_list:
    print(k)
