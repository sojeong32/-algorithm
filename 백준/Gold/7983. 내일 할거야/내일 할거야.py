import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1], reverse=True) #2차원 배열에서 [di,ti]라면 ti에 대해 역정렬

ans = arr[0][1] - arr[0][0]
for i in range(1, n):
    start = arr[i][1] - arr[i][0]
    if arr[i][1] <= ans:
        ans = start
    else:
        ans -= arr[i][0]

print(ans)