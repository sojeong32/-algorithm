from collections import deque

T = int(input())
for t in range(T):
    func = input()
    n = int(input())
    arr = input()
    if func.count('D') > n:  # 제거해야할 수가 배열의 수보다 많을 때
        print('error')  # error 출력
        continue
    arr = arr[1:-1]  # '['와 ']' 제거
    arr = deque(arr.split(',')) #  ','를 기준으로 나누고 덱으로 변환
    cnt = 0
    for j in func:
        if j == 'R':
            cnt += 1
        if j == 'D':
            if cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()

    if cnt % 2 == 1:
        arr.reverse()
    ans = '['+','.join(arr)+']'
    print(ans)
