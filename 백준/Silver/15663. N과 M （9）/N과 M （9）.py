n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = [0]*n
ans = []

def backtracking():
    if len(ans) == m:
        print(*ans)
        return

    check = 0
    for i in range(n):
        if not visited[i] and arr[i] != check:
            visited[i] = 1
            ans.append(arr[i])
            check = arr[i]
            backtracking()
            ans.pop()
            visited[i] = 0

backtracking()