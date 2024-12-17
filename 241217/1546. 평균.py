n = int(input())
arr = list(map(int, input().split()))

max_num = 0
for i in range(n):
    if arr[i] > max_num:
        max_num = arr[i]

for j in range(n):
    arr[j] = arr[j] / max_num * 100

print(sum(arr)/n)
