N = int(input())
data = input()
items = [int(input()) for _ in range(N)]


#영문자와 일치되는 숫자로 새로운 후위표기식 만들기
alphabet_list = []
for i in data:
    if i not in '*/+-' and i not in alphabet_list: #연산자가 아닐 때, 중복되지 않은 알파벳만 넣음
        alphabet_list.append(i)

alphabet_dict = {}
for i in range(len(alphabet_list)):
    alphabet_dict[alphabet_list[i]] = items[i]
# print(alphabet_dict)

new_data = []
for i in data:
    if i in '*/+-':
        new_data.append(i)
    else:
        new_data.append(str(alphabet_dict[i]))

#후위표기식을 계산하기
stack = []
for i in new_data:
    if i in '*/+-':
        if len(stack) <= 1:
            break

        else:
            x = float(stack.pop())
            y = float(stack.pop())

            if i == '*':
                result = y * x
                stack.append(result)

            elif i == '/':
                result = y / x
                stack.append(result)

            elif i == '+':
                result = y + x
                stack.append(result)

            elif i == '-':
                result = y - x
                stack.append(result)
    else:
        stack.append(i)

ans = stack.pop()
print(f'{ans:.2f}')