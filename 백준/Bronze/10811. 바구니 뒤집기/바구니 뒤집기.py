N, M = map(int, input().split())

basket = []
for n in range(1,N+1):
    basket.append(n)

for _ in range(M):
    i, j = map(int, input().split())
    for k in range((j-i+1)//2):
        basket[(i-1)+k], basket[(j-1)-k] = basket[(j-1)-k], basket[(i-1)+k]
print(*basket)