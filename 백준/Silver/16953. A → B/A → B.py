a, b = map(int, input().split())

ans = -1
count = 1
num = b
while num > a:
    if num % 10 == 1:
        num = num//10
        count += 1
    elif num % 2 == 0:
        num = num//2
        count += 1
    else:
        break

    if num == a:
        ans = count
print(ans)