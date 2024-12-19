n, k = map(int, input().split())

# 이항계수: n!/(k!*(n-k)!)

ans = 1

for i in range(1, n + 1):
    ans *= i

for j in range(1, k + 1):
    ans /= j

for k in range(1, n - k + 1):
    ans /= k

print(int(ans))