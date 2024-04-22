import sys

N, Q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
dp = [0]*(N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + arr[i-1]

for _ in range(Q):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[e]-dp[s-1])
