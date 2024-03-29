N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key= lambda x: [x[1], x[2], x[3]], reverse=True)

for i in range(N):
    if arr[i][0] == K:
        idx = i
        
for j in range(N):
    if arr[idx][1:] == arr[j][1:]:
        print(j+1)
        break