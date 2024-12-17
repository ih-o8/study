n, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for num in arr:
    if num < x:
        ans.append(num)
print(*ans)