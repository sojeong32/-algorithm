N = int(input())
data = list(map(int, input().split()))

sum_v = 0
ans = 0
for i in range(N-1):
    if data[i] < data[i+1]:
        sum_v += (data[i+1]-data[i])

    else:
        if ans < sum_v:
            ans = sum_v
        sum_v = 0
if ans < sum_v:
    ans = sum_v

print(ans)