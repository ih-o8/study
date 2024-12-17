n, m = map(int, input().split())
arr = [[0]] * n

for i in range(n):
    arr[i] = list(map(int, input().split()))

for j in range(n):
    lst = list(map(int, input().split()))
    for k in range(m):
        arr[j][k] += lst[k]

for l in range(n):
    print(*arr[l])