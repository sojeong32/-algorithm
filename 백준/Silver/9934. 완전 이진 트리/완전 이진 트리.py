k = int(input())
arr = list(map(int, input().split()))
ans = [[] for _ in range(k)]  # 해당되는 노드 넣는 칸 생성

def tree(arr, level):
    middle = len(arr)//2
    ans[level].append(arr[middle])
    if len(arr) == 1:
        return
    tree(arr[:middle], level+1)
    tree(arr[middle+1:], level+1)


tree(arr, 0)
for i in ans:
    print(*i)