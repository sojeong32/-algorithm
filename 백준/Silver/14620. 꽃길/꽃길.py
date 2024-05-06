def check(si, sj, visited):
    for k in range(5):
        ni = si + di[k]
        nj = sj + dj[k]
        if not (0 <= ni < N and 0 <= nj < N and not visited[ni][nj]):
            return False

    return True


def cal_sum(si, sj):
    sum_v = 0
    for k in range(5):
        ni = si + di[k]
        nj = sj + dj[k]
        sum_v += field[ni][nj]
    return sum_v


def flower(r, cnt, visited, S):
    global result
    if cnt == 3:
        result = min(result, S)
        return

    for i in range(r, N-1):
        for j in range(1, N-1):
            if check(i, j, visited):
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = 1
                flower(i, cnt+1, visited, S+cal_sum(i, j))

                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = 0


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
di = [0, 0, 1, 0, -1]
dj = [0, 1, 0, -1, 0]
result = 20001

flower(1, 0, visited, 0)
print(result)
