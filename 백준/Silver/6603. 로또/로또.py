while True:
    k, *S = map(int, input().split())
    if k == 0:
        break

    def backtracking(length, ans):
        if length == 6:
            print(*ans)
            return

        else:
            for i in range(length, k):
                if ans and ans[-1] >= S[i]:
                    continue
                backtracking(length+1, ans+[S[i]])


    backtracking(0, [])
    print()
