# 벌집 1개 > 6개 > 12개 > 18개 > 24개 증가

n = int(input()) - 1
cnt = 1
i = 1

while n > 0:
    if n >= 6 * i:
        n -= 6 * i
        cnt += 1
        i += 1
    else:
        cnt += 1
        break

print(cnt)