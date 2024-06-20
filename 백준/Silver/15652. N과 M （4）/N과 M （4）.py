def nnm():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n+1):
        if not ans or i >= ans[-1]:
            ans.append(i)
            nnm()
            ans.pop()

n, m = map(int, input().split())
ans = []

nnm()