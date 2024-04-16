N, K, T = map(int, input().split())
shark_size = list(map(int, input().split()))
shark_size.sort(reverse=True)

stack = []
count = 0

while count < K:
    if shark_size and shark_size[-1] < T:
        stack.append(shark_size.pop())
    else:
        if stack:
            T = T + stack.pop()
            count += 1

        else:
            break

print(T)
