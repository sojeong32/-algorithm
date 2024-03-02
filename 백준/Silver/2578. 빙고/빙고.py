# 빙고판과 빙고판과 같은 빈 빙고판 생성
arr = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]

# 부르는 숫자를 2차원 배열로 생성
num = [list(map(int, input().split())) for _ in range(5)]

count = 0  # 부르는 숫자의 순서를 알기 위해 초기값 설정
cnt = 0  # 빙고 줄 초기값 설정
flag3 = 0  # 전체적인 반복문 빠져나오기 위해 사용
for x in range(5):  # arr 범위
    for y in range(5):
        flag = 0
        for i in range(5):  # num 범위
            for j in range(5):
                if num[x][y] == arr[i][j]:  # 빙고판과 부르는 숫자가 같을 경우
                    visited[i][j] = 1  # 빙고판과 같은 빈 행렬에 1로 색칠
                    flag = 1
                    break

            if flag:
                break
        cnt = 0
        count += 1

        if count < 12:  # 빙고가 되기 위해서 3줄이 색칠이 되어 있어야 해서 부르는 숫자는 13이상이어야 함
            continue

        for r in range(5):
            sum_v = 0
            for c in range(5):
                if visited[r][c] == 1:  # 가로 탐색하면서 색칠된 곳 갯수 세기
                    sum_v += 1
                    if sum_v == 5:  # 가로 색칠된 곳이 5라면 한 줄 빙고
                        cnt += 1
                        if cnt >= 3:  # 3줄 빙고가 완성됐다면 빠져나오기
                            flag3 = 1
                            break
            if flag3:
                break
        if flag3:
            break
            # sum_v = 0  # 가로 한 줄 탐색했으면 0으로 초기화

        flag2 = 0

        for c in range(5):
            sum_v = 0
            for r in range(5):
                if visited[r][c] == 1:  # 세로 탐색하면서 색칠된 곳 갯수 세기
                    sum_v += 1
                    if sum_v == 5:  # 세로 색칠된 곳이 5라면 한 줄 빙고
                        cnt += 1
                        if cnt >= 3:  # 3줄 빙고가 완성됐다면 빠져나오기
                            flag3 = 1
                            break

            if flag3:
                break
        if flag3:
            break

        sum_v = 0
        for c in range(5):
            if visited[c][c] == 1:  # 대각선 탐색하면서 색칠된 곳 갯수 세기
                sum_v += 1
                if sum_v == 5:  # 대각선 색칠된 곳이 5라면 한 줄 빙고
                    cnt += 1
                    if cnt >= 3:  # 3줄 빙고가 완성됐다면 빠져나오기
                        flag3 = 1
                        break
            # if flag3:
            #     break
        if flag3:
            break

        sum_v = 0

        for c in range(5):
            if visited[(c)][-(c + 1)] == 1:  # 역대각선 탐색하면서 색칠된 곳 갯수 세기
                sum_v += 1
                if sum_v == 5:  # 역대각선 색칠된 곳이 5라면 한 줄 빙고
                    cnt += 1
                    if cnt >= 3:  # 3줄 빙고가 완성됐다면 빠져나오기
                        flag3 = 1
                        break

        if flag3:
            break
    if flag3:
        break

print(count)