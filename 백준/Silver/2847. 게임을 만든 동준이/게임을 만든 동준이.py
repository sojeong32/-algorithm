N = int(input())
score = [int(input()) for _ in range(N)]
count = 0

for i in range(N-1, 0, -1):
    while score[i] <= score[i-1]:
        score[i-1] -= 1
        count += 1

print(count)