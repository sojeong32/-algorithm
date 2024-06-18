N = int(input())
numbers = list(map(int, input().split()))
count = [0]*N

for idx in range(N):
    for i in range(1, 1001):
        if i > numbers[idx]:
            break
        if numbers[idx] % i == 0:
            count[idx] += 1
print(count.count(2))