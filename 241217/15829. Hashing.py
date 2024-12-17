m = 1234567891
n = int(input())
string = input()

ans = 0

for i in range(n):
    ans += (ord(string[i]) - 96) * (31 ** i)

print(ans % m)