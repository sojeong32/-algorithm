n = int(input())
wine = [0]+[int(input()) for _ in range(n)]

dp = [0]*(n+1)
dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1]+wine[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])
    # 현재 포도주 안 마신 경우, 현재는 마시고 전 것만 안 마신 경우, 현재와 전 것 마시고 전전것 안 마신 경우

print(dp[n])