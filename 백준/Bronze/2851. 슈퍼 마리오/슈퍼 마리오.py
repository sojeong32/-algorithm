sum_v = 0
over_v = 0
under_v = 0
for i in range(10):
    num = int(input())
    sum_v += num
    # print(sum_v)
    if sum_v >= 100:
        over_v, under_v = sum_v, sum_v - num
        # print(over_v, under_v)
        break
if sum_v < 100:
    under_v = sum_v

if abs(over_v - 100) - abs(under_v - 100) > 0:
    print(under_v)
else:
    print(over_v)

