import sys

X, N = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*(X+1)

for i in range(1, X+1):
    if i <= N:
        dp[i] = dp[i-1] + arr[i-1]
    else:
        dp[i] = dp[i-1] - arr[i-1-N] + arr[i-1]

if max(dp) == 0:
    print('SAD')
else:
    print(max(dp))
    print(dp.count(max(dp)))