# 그리디

n, k = map(int, input().split())
coin = [0] * n
for i in range(n):
    coin[i] = int(input())

cnt = 0

for j in range(n - 1, -1, -1):
    if k // coin[j]:
        cnt += k // coin[j]
        k = k % coin[j]

print(cnt)