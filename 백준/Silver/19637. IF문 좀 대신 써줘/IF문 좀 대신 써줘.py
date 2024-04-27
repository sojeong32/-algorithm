import sys

N, M = map(int, sys.stdin.readline().split())
power_list = []

for i in range(N):
    title, power = sys.stdin.readline().split()
    power = int(power)
    power_list.append([title, power])

for k in range(M):
    power = int(sys.stdin.readline())
    s, e = 0, N-1
    while s <= e:
        middle = (s+e)//2
        if power > power_list[middle][1]:
            s = middle + 1
        elif power <= power_list[middle][1]:
            e = middle - 1
        else:
            break

    ans = s
    print(power_list[ans][0])