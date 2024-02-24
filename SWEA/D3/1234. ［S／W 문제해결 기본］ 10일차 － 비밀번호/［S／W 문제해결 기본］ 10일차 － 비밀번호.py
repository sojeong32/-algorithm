for t in range(10):
    N, data = input().split()

    # data_list = list(map(int, data))

    stack = []
    for i in data:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    
    print(f'#{t+1}', ''.join(stack))
