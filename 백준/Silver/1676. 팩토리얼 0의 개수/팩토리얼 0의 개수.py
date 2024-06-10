n = int(input())

dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
    dp[i] = dp[i-1]*i

num = str(dp[n])
ans = 0
for j in range(len(num)-1, -1, -1):
    if num[j] == '0':
        ans += 1
    else:
        break
print(ans)