from collections import deque
import sys

T = int(input())
for t in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited = [0] * 10001
    q = deque()
    q.append([A, ''])
    visited[A] = 1
    while q:
        num, command = q.popleft()
        if num == B:
            print(command)
            break

        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = 1
            q.append([d, command+'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = 1
            q.append([s, command+'S'])

        l = (num % 1000) * 10 + num // 1000
        if not visited[l]:
            visited[l] = 1
            q.append([l, command+'L'])

        r = (num % 10) * 1000 + num // 10
        if not visited[r]:
            visited[r] = 1
            q.append([r, command+'R'])