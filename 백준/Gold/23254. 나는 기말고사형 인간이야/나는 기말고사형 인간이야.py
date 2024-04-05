import sys

n, m = map(int, sys.stdin.readline().split())
base_score = list(map(int, sys.stdin.readline().split()))
plus_score = list(map(int, sys.stdin.readline().split()))

total_time = 24 * n  
plus_list = []
for i in range(m):
    study_time = (100-base_score[i]) // plus_score[i]
    plus_list.append((plus_score[i], study_time))
    plus_list.append((((100-base_score[i]) % plus_score[i]), 1))

ans = sum(base_score)
plus_list.sort(reverse=True)
for i in range(len(plus_list)):
    ans += plus_list[i][0] * min(plus_list[i][1], total_time)
    total_time -= min(plus_list[i][1], total_time)

print(ans)
