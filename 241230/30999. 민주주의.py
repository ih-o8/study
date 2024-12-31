n, m = map(int, input().split())
ans = 0
mid = m // 2

for _ in range(n):
    score = input()
    cnt = 0
    for i in score:
        if cnt > mid:
            break
        if i =='O':
            cnt += 1
    if cnt > mid:
        ans += 1

print(ans)