T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())

    floor = str(N % H)    #층 구하기
    number = str((N // H) + 1).zfill(2)   #호 구하기(2자리 수로 표현)

    if floor == '0':         #맨 꼭대기층의 경우 나눴을 때 나머지가 0이 되므로
        floor = str(H)       #층수는 맨 위, 호수는 1을 빼준다
        number = str(N // H).zfill(2)

    print(floor+number)