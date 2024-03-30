N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, max(arr)

while s <= e:
    middle = (s+e)//2
    ans = 0
    for i in arr:
        if i >= middle:
            ans += i-middle

    if ans >= M:
        s = middle+1
    else:
        e = middle-1
print(e)