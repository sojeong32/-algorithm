width, length = map(int, input().split())  # 혹시 종이자르는 범위가 벗어나지는 않겠지?
N = int(input())
cut_list = [[0],[0]]  # 가로, 세로의 초기값이 있는 리스트 생성

for n in range(N):
    func, data = map(int, input().split())
    if func == 0:  # 가로로 잘라야 할 인덱스 추가하기(세로길이구하기)
        cut_list[0].append(data)
    if func == 1:  # 세로로 잘라야 할 인덱스 추가하기(가로길이구하기)
        cut_list[1].append(data)
cut_list[0].append(length)   # 가로, 세로의 끝값 추가
cut_list[1].append(width)

for i in cut_list:  # 2차원 배열 정렬하기
    i.sort()
# print(cut_list)

length_list = []
for i in range(len(cut_list[0])-1):  # 세로 리스트 탐색하면서 세로 길이 구하기
    length_list.append(cut_list[0][i+1] - cut_list[0][i])
# print(length_list)

width_list = []
for j in range(len(cut_list[1])-1):  # 가로 리스트 탐색하면서 가로 길이 구하기
    width_list.append(cut_list[1][j+1] - cut_list[1][j])
# print(width_list)


area = max(width_list) * max(length_list)  #길이 리스트에서 큰 값만을 추출해서 곱해 제일 큰 영역 구하기

print(area)