data = list(map(int, input().split()))

info1 = [1, 2, 3, 4, 5, 6, 7, 8]
info2 = info1[::-1]

if data == info1:
    print('ascending')
elif data == info2:
    print('descending')
else:
    print('mixed')