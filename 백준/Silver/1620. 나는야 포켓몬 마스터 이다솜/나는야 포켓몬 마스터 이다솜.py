import sys
n, m = map(int, input().split())
dict = {}
for i in range(1, n+1):
    dict[str(i)] = sys.stdin.readline().rstrip()
convert_dict = {v:k for k,v in dict.items()} # 딕셔너리에서 key와 value값의 위치를 바꾼 새 딕셔너리 만드는 코드
for j in range(m):
    val = sys.stdin.readline().rstrip()
    if val in dict:
        print(dict[val])
    else:
        print(convert_dict[val])