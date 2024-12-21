import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = input().split()
    arr[i][0] = int(arr[i][0])

arr.sort(key=lambda x: x[0])

for j in arr:
    print(*j)