def omok(player):
    global ans
    for c in range(19):
        for r in range(19):
            if arr[r][c] == player:  # 검은색이고 방문안한 위치에서
                for k in range(4):
                    i = r
                    j = c
                    count = 0
                    while 0 <= i < 19 and 0 <= j < 19 and arr[i][j] == player:
                        count += 1
                        i = i + di[k]
                        j = j + dj[k]
                        if count == 5:
                            if 0 <= r - di[k] < 19 and 0 <= c - dj[k] and arr[r-di[k]][c-dj[k]] == player:
                                continue
                            elif 0 <= i < 19 and 0 <= j < 19 and arr[i][j] == player:
                                continue
                            else:
                                ans = player
                                result.append(r + 1)
                                result.append(c + 1)
                                return ans

arr = [list(map(int, input().split())) for _ in range(19)]

di = [0, 1, 1, -1]  #우, 하, 4시, 2시 방향설정
dj = [1, 0, 1, 1]
ans = 0
result = []

omok(1)
omok(2)

if ans != 0:
    print(ans)
    print(*result)
else:
    print(ans)