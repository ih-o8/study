fibo = [(1,0), (0,1)] + [0] * 39
for i in range(2,41):
    fibo[i] = (fibo[i-2][0] + fibo[i-1][0], fibo[i-2][1] + fibo[i-1][1])

for _ in range(int(input())):
    print(*fibo[int(input())])