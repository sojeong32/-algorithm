arr = [list(map(int, input().split())) for _ in range(9)]

arr.sort() # 출력이 오름차순이어야 하므로 처음부터 정렬
# print(arr)


# 아홉난쟁이 키의 합 구하기
sum_height = 0
for a in arr:
    sum_height += a[0]
# print(sum_height)

# 아홉난쟁이에서 두 난쟁이의 키의 합을 뺀 값이 100인 두 난쟁이의 키 구하기
for i in range(9):
    for j in range(i+1, 9):
        if sum_height - (arr[i][0] + arr[j][0]) == 100:
            # print(arr[i][0], arr[j][0])
            remove1 = arr[i]  #제거값 2개 구하기
            remove2 = arr[j]

# k를 돌면서 제거값이면 패스 아니면 출력
for k in arr:
    if k == remove1 or k == remove2:
        pass
    else:
        print(*k)