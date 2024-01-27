data = input()

index_data = {'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':'','j':'','k':'','l':'',
              'm':'','n':'','o':'','p':'','q':'','r':'','s':'','t':'','u':'','v':'','w':'','x':'','y':'','z':''}


for i in index_data:
    if i in data:
        index_data[i] = data.index(i)
        # print(data.index(i))
        # print(type(data.index(i)))
    else:
        index_data[i] = -1

print(*index_data.values())