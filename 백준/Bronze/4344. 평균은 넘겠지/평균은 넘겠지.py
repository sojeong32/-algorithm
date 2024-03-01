T = int(input())
for t in range(T):
    N, *data = list(map(int,input().split())) # 패킹
    # print(data)

    count = 0
    average = sum(data)/N
    for i in data:
        if i > average:
            count += 1
    print(f'{(count/N)*100:.3f}%')