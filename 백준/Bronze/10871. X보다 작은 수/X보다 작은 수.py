a, b = map(int,input().split())
data = map(int,input().split())

# print(b)
empty_list = []
for i in data:
    if i < b:
        empty_list.append(i)

print(*empty_list)