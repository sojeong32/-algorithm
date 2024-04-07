l, c = map(int, input().split())
alphabet = input().split()
alphabet.sort()


def check(arr):
    c_count = 0  # 자음 갯수
    v_count = 0  # 모음 갯수
    for i in arr:
        if i in 'aeiou':
            v_count += 1
        else:
            c_count += 1

    if c_count >= 2 and v_count >= 1:
        return True
    else:
        return False


def backtracking(arr):
    if len(arr) == l:
        if check(arr):
            print(''.join(arr))

    else:
        for j in range(len(arr), c):
            if arr[-1] < alphabet[j]:
                arr.append(alphabet[j])
                backtracking(arr)
                arr.pop()

for k in range(c-l+1):
    ans = [alphabet[k]]
    backtracking(ans)