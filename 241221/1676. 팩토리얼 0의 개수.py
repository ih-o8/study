import sys
input = sys.stdin.readline

num = 1

n = int(input())
if n > 1:
    for i in range(2, n + 1):
        num *= i

string = str(num)
cnt = 0

for j in range(len(string) - 1, -1, -1):
    if string[j] == '0':
        cnt += 1
    else:
        break

print(cnt)