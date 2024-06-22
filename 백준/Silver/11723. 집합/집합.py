import sys
n = int(input())
S = set()
for i in range(n):
    action = list(sys.stdin.readline().split())
    if len(action) == 1:
        if action[0] == 'all':
            S = set(i for i in range(1, 21))
        elif action[0] == 'empty':
            S = set()

    else:
        command, num = action[0], action[1]
        num = int(num)

        if command == 'add':
            S.add(num)
        elif command == 'remove':
            if num in S:
                S.remove(num)
        elif command == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)