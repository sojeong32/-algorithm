from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = deque([0]*w)

time = 0
while trucks:
    if sum(bridge)+trucks[0] <= L:
        time += 1
        bridge.popleft()
        truck = trucks.pop(0)
        bridge.append(truck)

    else:
        time += 1
        bridge.popleft()
        if sum(bridge) + trucks[0] <= L:
            truck = trucks.pop(0)
            bridge.append(truck)
        else:
            bridge.append(0)

print(time+w)