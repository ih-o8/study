import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [0] * (n+1)
for i in range(n):
    arr[i+1] = input().strip('\n')

for _ in range(m):
    name = input().strip('\n')
    if ord(name[0]) < 65:
        number = int(name)
        print(arr[number])
    else:
        for k in range(1, len(arr)):
            if arr[k] == name:
                print(k)