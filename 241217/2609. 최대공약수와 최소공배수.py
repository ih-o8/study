a, b = map(int, input().split())

max_num = 1

i = 2
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        max_num = i
    i += 1

print(max_num)
print(a * b // max_num)