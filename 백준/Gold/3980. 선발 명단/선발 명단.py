def backtracking(depth, sum_v):
    global max_v
    if depth == 11:
        max_v = max(max_v, sum_v)
        return

    for i in range(11):
        if not members[i] and ability[depth][i] != 0:
            members[i] = 1
            backtracking(depth+1, sum_v+ability[depth][i])
            members[i] = 0

T = int(input())
for t in range(T):
    ability = [list(map(int, input().split())) for _ in range(11)]
    members = [0]*11

    max_v = 0

    backtracking(0, 0)
    print(max_v)