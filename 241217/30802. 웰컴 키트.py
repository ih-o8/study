n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0

for i in arr:
    if i % t == 0:
        cnt += i // t
    else:
        cnt += i // t + 1

print(cnt)
print(f'{n // p} {n % p}')