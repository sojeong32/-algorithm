N = int(input())
top = -1
stack = []
data = []
for n in range(N):
    data.append(input().split())

for command in data:
    if command[0] == 'push':
        num = command[1]
        top += 1
        stack.append(int(num))
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            y = stack.pop()
            top -= 1
            print(y)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[top])