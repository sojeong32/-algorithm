T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    N_list = input().split()
    M_list = input().split()
    Q = int(input())
    print(f'#{t+1}', end=' ')
    for q in range(Q):
        Y = int(input())
        y_idxn = (Y % N) - 1
        y_idxm = (Y % M) - 1
        yn = N_list[y_idxn]
        ym = M_list[y_idxm]


        print(f'{yn+ym}', end=' ')
    print()