n = int(input())
arr = list(map(int, input().split()))
arr.sort()

note = [0] * n
ans = note[0] = arr[0]

for i in range(1, n):
    note[i] = note[i-1] + arr[i]
    ans += note[i]

print(ans)