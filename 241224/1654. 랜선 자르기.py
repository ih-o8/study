import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [0] * k
for i in range(k):
    arr[i] = int(input())

ans = min(arr)
if k == n:
    print(ans)
else:
    while True:
        cnt = 0
        for num in arr:
            cnt += num // ans
        if cnt >= n:
            break
        ans -= 1

    print(ans)