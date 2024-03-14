# 배

from collections import deque

n = int(input())
ships = deque(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)  # 박스를 역정렬


max_ship = max(ships)  # 배의 제한 무게 최댓값
count = 0
while boxes and max_ship >= boxes[0]:  # 박스가 남아 있고 배의 제한 무게 최댓값이 박스 최대무게보다 클 때
    count += 1
    for i in range(n):
        weight = ships.popleft()
        for j in range(len(boxes)):
            if weight >= boxes[j]:
                boxes.remove(boxes[j])
                break
        ships.append(weight)

if len(boxes) == 0:
    print(count)
else:
    print(-1)