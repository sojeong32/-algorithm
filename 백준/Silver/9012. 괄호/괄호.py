T = int(input())
for t in range(T):
    arr = list(input())
    stack = []
    ans = 'YES'
    for char in arr:
        if char == '(':
            stack.append(char)
        else:
            if '(' in stack:
                stack.pop()
            else:
                ans = 'NO'
                break

    if stack:
        ans = 'NO'

    print(ans)