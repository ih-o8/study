arr = list(range(1, 31))

for _ in range(28):
    n = int(input())
    for i in range(len(arr)):
        if arr[i] == n:
            arr.pop(i)
            break

print(arr[0])
print(arr[1])