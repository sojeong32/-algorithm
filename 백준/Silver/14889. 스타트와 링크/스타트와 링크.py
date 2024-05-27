N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N

min_v = 40001
def backtracking(depth, idx):
    global min_v

    if depth == N//2:
        sum_start, sum_link = 0, 0
        for j in range(N):
            for k in range(N):
                if visited[j] and visited[k]:
                    sum_start += ability[j][k]
                if not visited[j] and not visited[k]:
                    sum_link += ability[j][k]
        min_v = min(min_v, abs(sum_start-sum_link))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            backtracking(depth+1, i+1)
            visited[i] = 0

backtracking(0, 0)
print(min_v)