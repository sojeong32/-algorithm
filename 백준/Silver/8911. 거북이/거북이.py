import copy

T = int(input())
for t in range(T):
    actions = list(input())
    location = [[0, 0]]
    di = [1, 0, -1, 0]  # 북, 동, 남, 서 방향설정
    dj = [0, 1, 0, -1]
    cur = [0, 0]
    dir = 0

    for action in actions:
        if action == 'F':
            cur[0] = cur[0] + dj[dir]  # 앞으로 이동
            cur[1] = cur[1] + di[dir]
            location.append(copy.deepcopy(cur))
        elif action == 'B':
            cur[0] = cur[0] - dj[dir]  # 뒤로 이동
            cur[1] = cur[1] - di[dir]
            location.append(copy.deepcopy(cur))
        elif action == 'L':
            dir = (dir - 1) % 4  # 방향 좌회전
        elif action == 'R':
            dir = (dir + 1) % 4  # 방향 우회전

    max_x = max(location, key=lambda x: x[1])[1] # x의 최고값
    min_x = min(location, key=lambda x: x[1])[1] # x의 최저값
    max_y = max(location, key=lambda x: x[0])[0] # y의 최고값
    min_y = min(location, key=lambda x: x[0])[0] # y의 최저값

    length_x = abs(max_x-min_x) # x선분 길이
    length_y = abs(max_y-min_y) # y선분 길이
    area = length_x * length_y  # 넓이
    print(area)
