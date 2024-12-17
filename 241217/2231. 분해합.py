n = int(input())

for i in range(n):
    ans = i + sum(map(int, str(i)))
    if ans == n:
        print(i)
        break
else:
    print(0)