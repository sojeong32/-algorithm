def n_m():
    if len(arr) == M:
        print(*arr)
        return
    else:
        for i in range(1, N+1):
            arr.append(i)
            n_m()
            arr.pop()

N, M = map(int, input().split())

arr = []
n_m()