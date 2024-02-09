T = int(input())
for t in range(T):
    data = input()+'X'
    sum_val = 0
    count = 0
    prev = 0
    for i in data:

        if i == 'O':
            count += 1
            prev += count
        else:
            count = 0

    sum_val += prev
            
    print(sum_val)