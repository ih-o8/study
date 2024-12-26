import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [0] * k
for i in range(k):
    arr[i] = int(input())

start, end = 1, max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)  # 랜선의 최대 길이