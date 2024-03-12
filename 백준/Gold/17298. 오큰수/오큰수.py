N = int(input())
arr = list(map(int, input().split()))

check = [-1]*N
stack = [0]

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        check[stack.pop()] = arr[i]
    stack.append(i)

print(*check)