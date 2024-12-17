n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in arr:
    if i > 2:
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1:
                cnt += 1
    elif i == 2:
        cnt += 1

print(cnt)