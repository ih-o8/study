arr = []
cnt = 0
for _ in range(10):
    num = int(input()) % 42
    if num not in arr:
        arr.append(num)
        cnt += 1
print(cnt)