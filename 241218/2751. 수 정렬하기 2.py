import sys
input = sys.stdin.readline

arr = [0] * 1000001

for i in range(int(input())):
    num = int(input())
    if num >= 0:
        arr[num] += 1
    else:
        arr[-num] += 10

for j in range(1000000, 0, -1):
    if arr[j] >= 10:
        print(-j)
for k in range(1000001):
    if arr[k] == 1 or arr[k] == 11:
        print(k)