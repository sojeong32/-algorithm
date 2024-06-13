import sys
sys.setrecursionlimit(10**6)

def check():
    global mid_res

    if len(mid_res) == n and int(mid_res) > int(x):  # 글자 수가 n와 같고 만들어진 숫자가 x보다 크다면
        result.add(int(mid_res))  # result에 추가
        return

    for i in range(n):
        if visited[i] == 0:
            mid_res += x[i]
            visited[i] = 1
            check()
            mid_res = mid_res[:-1]
            visited[i] = 0

x = input()
n = len(x)  # x 길이
visited = [0]*n  # 구성을 같게 하기 위한 방문리스트 설정
result = set()
mid_res = ''

check()
result = list(result)
result.sort()

if len(result) == 0:
    print(0)
else:
    print(result[0])

