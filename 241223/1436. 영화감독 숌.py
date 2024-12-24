n = int(input())
cnt = 0
number = 666
while cnt < n:
    if '666' in str(number):
        cnt += 1
    if cnt == n:
        break
    number += 1

print(number)