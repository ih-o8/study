import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = list(map(int, input().split()))

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1])

for j in arr:
    print(*j)