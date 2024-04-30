N, M = map(int, input().split())

dp = [[[1000, 1000, 1000] for _ in range(M)] for _ in range(N)]
fuel = [list(map(int, input().split())) for _ in range(N)]
for i in range(M):
    dp[0][i] = [fuel[0][i], fuel[0][i], fuel[0][i]]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if (j == 0 and k == 2) or (j == M-1 and k == 0):
                continue
            for l in range(3):
                if k == l:
                    continue
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-k+1][l]+fuel[i][j])

min_v = 1000
for i in range(M):
    min_v = min(min(dp[N-1][i]), min_v)
print(min_v)