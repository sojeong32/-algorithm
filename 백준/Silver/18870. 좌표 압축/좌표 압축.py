n = int(input())
arr = list(map(int, input().split()))
filter_arr = list(set(arr))
filter_arr.sort()
dict = {}
for i in range(len(filter_arr)):
    dict[filter_arr[i]] = i
ans = []
for j in arr:
    ans.append(dict[j])
print(*ans)