N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
K = int(input())


idx = [list(map(int, input().split())) for _ in range(K)]

for _ in idx:
    i,j,x,y = _
    sum_val = 0
    for r in range(i-1, x):
        for c in range(j-1, y):
            sum_val += data[r][c]

    print(sum_val)