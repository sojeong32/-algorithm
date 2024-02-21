N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

new = [[0]*M for _ in range(N)] #빈 행렬 만들고 거기에 더한 값 채우기
for i in range(N):
    for j in range(M):
        new[i][j] = A[i][j] + B[i][j]

for k in range(N):
    print(*new[k])