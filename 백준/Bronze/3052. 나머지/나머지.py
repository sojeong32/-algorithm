empty_list = []
for i in range(10):
    data = int(input())
    empty_list.append(data)

# print(empty_list)

empty_dict = {}
for j in empty_list:
    if j % 42 not in empty_dict:
        empty_dict[j % 42] = 1
    else:
        empty_dict[j % 42] += 1
# print(empty_dict)
print(len(empty_dict.keys()))