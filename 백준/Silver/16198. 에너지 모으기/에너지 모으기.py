def energy():
    global ans, sum_v
    if len(weight) == 2:
        ans = max(ans, sum_v)
        return

    for i in range(1, len(weight)-1):
        sum_v = sum_v + weight[i-1] * weight[i+1]
        x = weight.pop(i)
        energy()
        weight.insert(i, x)
        sum_v = sum_v - weight[i-1] * weight[i+1]

n = int(input())
weight = list(map(int, input().split()))
ans = 0
sum_v = 0

energy()
print(ans)