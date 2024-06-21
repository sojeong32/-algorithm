n = int(input())
dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    if i == 1:
        dp[1] = 3
        continue
    dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
print(dp[n])