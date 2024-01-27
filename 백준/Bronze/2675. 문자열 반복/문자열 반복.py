data = [input().split() for _ in range(int(input()))]


for i in data:
    j_list = []
    for j in i[1]:
        j_list.append(j*int(i[0]))

    print(''.join(j_list))