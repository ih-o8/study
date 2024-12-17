a = int(input())
b = int(input())
c = int(input())

ans = str(a * b * c)
for i in range(10):
    cnt = 0
    for j in ans:
        if str(i) == j:
            cnt += 1
    print(cnt)