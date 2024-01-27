num = int(input())

empty_list = []
for _ in range(int(num)):
    empty_list.append(input().split())


for i in empty_list:
    j_list = []
    for j in i[1]:
        j_list.append(j*int(i[0]))

    print(''.join(j_list))