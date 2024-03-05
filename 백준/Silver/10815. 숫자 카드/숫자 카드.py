N = int(input())
n_list = map(int, input().split())
M = int(input())
m_list = map(int, input().split())


empty_dict = {}
for n in n_list:
    empty_dict[n] = 1

for m in m_list:
    if m in empty_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
    