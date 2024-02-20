A, B = input().split()

for i in A:
    if i in B:
        result = (A.index(i), B.index(i))
        break


arr = [['.'] * len(A) for _ in range(len(B))]

for i in range(len(A)):
    arr[result[1]][i] = A[i]
for j in range(len(B)):
    arr[j][result[0]] = B[j]

for k in arr:
    print(''.join(k))