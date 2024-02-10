n = int(input())

f = [0]*(1001)

f[1] = 1
f[2] = 3

for i in range(3, n+1):
    f[i] = f[i-2]*2 + f[i-1]

print(f[n] % 10007)