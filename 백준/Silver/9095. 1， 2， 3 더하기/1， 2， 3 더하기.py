T = int(input())
for t in range(T):
    n = int(input())
    dp = [0] * (n+1)
    if n == 0:
        print(0)
        continue
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(2)
        continue
    if n == 3:
        print(4)
        continue
    for i in range(4, n+1):
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n])