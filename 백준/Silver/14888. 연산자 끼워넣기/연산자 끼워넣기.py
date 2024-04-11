N = int(input())
numbers = list(map(int, input().split()))
symbols = list(map(int, input().split()))

min_val = 1000000000
max_val = -1000000000

def cal(idx, val, plus, minus, multiply, divide):
    global min_val, max_val

    if idx == N:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    if plus:
        cal(idx+1, val+numbers[idx], plus-1, minus, multiply, divide)
    if minus:
        cal(idx+1, val-numbers[idx], plus, minus-1, multiply, divide)
    if multiply:
        cal(idx+1, val*numbers[idx], plus, minus, multiply-1, divide)
    if divide:
        cal(idx+1, int(val/numbers[idx]), plus, minus, multiply, divide-1)


cal(1, numbers[0], symbols[0], symbols[1], symbols[2], symbols[3])
print(max_val)
print(min_val)