#세로읽기

data = [list(input()) for _ in range(5)]


result = ''
for i in range(15):
    for j in range(5):
        try:
            result += data[j][i]
        except IndexError:
            result += ''

print(result)