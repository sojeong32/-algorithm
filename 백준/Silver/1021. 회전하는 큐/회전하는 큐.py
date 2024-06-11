from collections import deque

n, m = map(int, input().split())
position = deque(map(int, input().split()))
queue = deque(i for i in range(1, n+1))

ans = 0
while position:
    j = position.popleft()
    if j == queue[0]:
        queue.popleft()
    else:
        if queue.index(j) <= len(queue)//2:
            k = queue.popleft()
            queue.append(k)
            ans += 1
        else:
            k = queue.pop()
            queue.appendleft(k)
            ans += 1
        position.appendleft(j)
print(ans)