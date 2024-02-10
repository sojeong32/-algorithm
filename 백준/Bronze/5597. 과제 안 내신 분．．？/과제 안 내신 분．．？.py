empty_list = []
for i in range(28):
    data = input()
    empty_list.append(data)
    empty_list.sort()

for k in range(1,31):
    if str(k) not in empty_list:
        print(k)