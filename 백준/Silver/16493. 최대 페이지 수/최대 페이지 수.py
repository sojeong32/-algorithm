N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

def maxpage(level, day, sum_page):
    if day <= N:
        ans.append(sum_page)


    if level == M:
        return

    maxpage(level+1, day+arr[level][0], sum_page+arr[level][1])
    maxpage(level+1, day, sum_page)

ans = []
maxpage(0, 0, 0)
print(max(ans))
