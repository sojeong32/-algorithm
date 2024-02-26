# n과 m(2)

def n_m():
    if len(lst) == M:
        a = sorted(lst)      # 고른 수열이 오름차순이어야 해서 오름차순으로 저장
        if a not in result:  # 빈 리스트(result)에 수열이 없을 경우에 append
            result.append(a)
            return

    else:
        for i in range(1, N+1):
            if i not in lst:
                lst.append(i)
                n_m()
                lst.pop()


N, M = map(int, input().split())
lst = []
result = []

n_m()

for i in range(len(result)):
    print(*result[i])