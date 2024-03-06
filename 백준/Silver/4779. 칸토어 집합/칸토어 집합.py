def f(x):
    if x == 1:
        return '-'
    else:
        left = f(x//3)
        center = ' '*(x//3)
        return left + center + left


while True:
    try:
        n = int(input())
        N = 3**n
        arr = f(3**n)
        print(arr)

    except EOFError:
        break
