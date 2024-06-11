import sys
sys.setrecursionlimit(10**6)

def dfs(si, sj):
    global ans, num6

    if len(num6) == 6:
        ans.add(num6)
        return

    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]

        if 0 <= ni < 5 and 0 <= nj < 5:
            num6 += arr[ni][nj]
            dfs(ni, nj)
            num6 = num6[:-1]

arr = [input().split() for _ in range(5)]
# print(arr)

ans = set()
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(5):
    for j in range(5):
        num6 = ''
        num6 += arr[i][j]
        dfs(i, j)

print(len(ans))