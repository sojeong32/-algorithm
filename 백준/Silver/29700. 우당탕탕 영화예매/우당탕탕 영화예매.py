n, m, k = map(int, input().split())
seat = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m-k+1):
        if seat[i][j:j+k] == ['0']*k:
            ans += 1
print(ans)
