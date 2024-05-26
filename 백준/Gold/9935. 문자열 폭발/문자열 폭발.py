import sys

arr = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()
ans = word[::-1]
stack = []

for i in range(len(arr)-1,-1,-1):
    stack.append(arr[i])
    if len(stack) >= len(word):
        if ''.join(stack[(-len(word)):]) == ans:
            for k in range(len(word)):
                stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack[::-1]))