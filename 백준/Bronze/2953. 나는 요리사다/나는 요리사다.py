arr = [list(map(int, input().split())) for _ in range(1,6)]

sum_list = []
for i in range(len(arr)):
    sum_list.append((i+1, sum(arr[i])))


# 튜플형태로 인덱스를 활용해 뽑는 것은 max함수가 적용이 안되는 듯
# max_v = max(sum_list[1])
# print(max_v)

#튜플에서 최댓값 구하기
max_v = 0
for j in sum_list:
    if max_v < j[1]:
        max_v = j[1]

#최댓값이 같을 때 출력
for k in sum_list:
    if max_v == k[1]:
        print(k[0], k[1])