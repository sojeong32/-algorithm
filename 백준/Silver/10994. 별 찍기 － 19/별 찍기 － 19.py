def star(num):
    if num == n:
        print(('*'+' ')*(num-1)+'*'+(' '+'*')*(num-1))
        return

    print(('*'+' ')*(num-1)+'**'*(n-num)+'*'+'**'*(n-num)+(' '+'*')*(num-1))
    print(('*'+' ')*(num)+'  '*(n-num-1)+' '+'  '*(n-num-1)+(' '+'*')*(num))
    star(num+1)
    print(('*'+' ')*(num)+'  '*(n-num-1)+' '+'  '*(n-num-1)+(' '+'*')*(num))
    print(('*'+' ')*(num-1)+'**'*(n-num)+'*'+'**'*(n-num)+(' '+'*')*(num-1))


n = int(input())
star(1)