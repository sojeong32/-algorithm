num = int(input())


count = 0
empty_list = []

while count < num:
    data = list(map(int,input().split()))
    empty_list.append(data)
    count += 1


for i in empty_list:
    A , B = i[0], i[1]
    print(A + B)