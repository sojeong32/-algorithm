n = int(input())
m = int(input())
adjl = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
q = []
for _ in range(m):
    i, j = map(int, input().split())
    adjl[i].append(j)
    adjl[j].append(i)

def bfs(num):
    q.append(num)
    visited[num] += 1
    while q:
        x = q.pop(0)
        for i in adjl[x]:
            if visited[i] != -1:
                continue
            visited[i] = visited[x]+1
            q.append(i)

bfs(1)
print(visited.count(1)+visited.count(2))  # 1은 친구를, 2는 친구의 친구를 나타냄
