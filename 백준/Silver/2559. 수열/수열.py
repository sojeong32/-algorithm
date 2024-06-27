n, k = map(int, input().split())
temperature = list(map(int, input().split()))
dp = [-101]*n
sum_v = 0
for i in range(k):
    sum_v += temperature[i]
dp[k-1] = sum_v
for j in range(k, n):
    dp[j] = dp[j-1]+temperature[j]-temperature[j-k]
print(max(dp[k-1:]))