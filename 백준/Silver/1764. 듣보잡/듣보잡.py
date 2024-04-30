import sys
N, M = map(int, input().split())
dict = {}
for _ in range(N):
    dict[sys.stdin.readline().rstrip()] = _
ans = []
for i in range(M):
    name = sys.stdin.readline().rstrip()
    if name in dict:
        ans.append(name)
ans.sort()
print(len(ans))
for k in ans:
    print(k)