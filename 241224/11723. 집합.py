import sys
input = sys.stdin.readline
s = [0] * 21

for _ in range(int(input())):
    arr = input().split()
    if len(arr) > 1:
        num = int(arr[1])

    if arr[0] == 'add':  # 추가
        if not s[num]:
            s[num] = 1

    elif arr[0] == 'remove':  # 제거
        if s[num]:
            s[num] = 0

    elif arr[0] == 'check':
        if s[num]:
            print(1)
        else:
            print(0)

    elif arr[0] == 'toggle':
        if s[num]:
            s[num] = 0
        else:
            s[num] = 1

    elif arr[0] == 'all':
        s = [0] + [1] * 20

    elif arr[0] == 'empty':
        s = [0] * 21