def virus_num(num):
    visited = [0]*(V+1)  #스택 만들기
    stack = []
    visited[num] = 1
    while True:
        for w in adjl[num]:
            if visited[w] == 0:
                stack.append(num)
                num = w
                visited[num] = 1

                break
        else:
            if stack:
                num = stack.pop()
            else:
                break
    return visited


V = int(input())
E = int(input())
adjl = [[] for _ in range(V+1)]
for _ in range(E):
    i, j = map(int, input().split())
    adjl[i].append(j)
    adjl[j].append(i)

# print(adjl)
print(virus_num(1).count(1)-1)