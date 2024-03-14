n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

profit = [0]*(n+1)
for i in range(n):
    for j in range(i+arr[i][0], n+1):
        if profit[j] < profit[i] + arr[i][1]:
            profit[j] = profit[i] + arr[i][1]
            
print(max(profit))