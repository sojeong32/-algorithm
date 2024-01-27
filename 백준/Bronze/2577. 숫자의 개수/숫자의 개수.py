A = int(input())
B = int(input())
C = int(input())

num = A*B*C

# print(num)

empty_dict = {}

for i in range(10):
    empty_dict[i] = 0
    for j in str(num):
        if str(i) == j:
            empty_dict[i] += 1
        else:
            continue
   
# print(empty_dict)
        
for k in empty_dict.keys():
    print(empty_dict[k])