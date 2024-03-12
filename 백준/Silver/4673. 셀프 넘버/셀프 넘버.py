def d(num):  # 생성자 num이 들어가며 셀프넘버가 아닌 수 구하는 함수
    n = str(num)
    for i in n:
        num += int(i)
    if num in arr:
        arr.remove(num)


arr = list(range(1, 10001))

for x in range(1, 10001):  #1부터 돌며 함수 실행
    d(x)
    
for k in arr:
    print(k)
