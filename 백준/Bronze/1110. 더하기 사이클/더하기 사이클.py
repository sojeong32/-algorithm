data = int(input())
num = data
count = 0
new_num = 0
found = True

while found:
    sum = (num // 10) + (num % 10)
    new_num = (num % 10) * 10 + (sum % 10)
    count += 1
    if data == new_num:
        found = False
        print(count)
        break
    else:
        num = new_num