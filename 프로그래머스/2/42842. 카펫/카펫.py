def solution(brown, yellow):
    answer = []
    yellows = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellows.append(i)
    print(yellows)

    n = len(yellows)
    for j in range(n):
        if (yellows[j]+yellows[n-1-j])*2+4 == brown:
            answer.append(yellows[n-1-j]+2)
            answer.append(yellows[j]+2)
            break
    return answer