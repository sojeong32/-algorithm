N = int(input())
number = int(input())
arr = list(map(int, input().split()))

# print(arr)
count = [0] * 101  # 학생 추천리스트
frame = []  # 사진틀
for i in arr:
    count[i] += 1
    if i in frame:
        continue
    elif len(frame) < N:
        frame.append(i)
    else:
        min_v = 1000
        for j in frame:
            if min_v > count[j]:
                min_v = count[j]
                erase = j

        frame.remove(erase)
        count[erase] = 0
        frame.append(i)

frame.sort()
print(*frame)
