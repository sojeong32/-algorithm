N, M = map(int, input().split())
data = list(map(int, input().split()))

max_v = 0
for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                sum_v = data[i] + data[j] + data[k]
                if  (sum_v <= M) and (sum_v > max_v):
                    max_v = sum_v
print(max_v)