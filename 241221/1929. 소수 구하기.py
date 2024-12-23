# 100 이하의 소수 구하는 방법
# 1 부터 100 까지의 자연수를 모두 나열
# 소수도 합성수도 아닌 1 제거
# 2 외의 2의 배수 제거, 3 외의 3의 배수 제거, 5 외의 5의 배수 제거 등 반복
# (100의 제곱근인 10 이하의 소수들에 대해서만 반복)


m, n = map(int, input().split())
arr = [0] * m + [1] * (n - m + 1)

if arr[1] == 1:
    arr[1] = 0

for i in range(2, int(n ** (1 / 2)) + 1):
    j = 2
    while i * j <= n:
        arr[i*j] = 0
        j += 1

for k in range(m, n + 1):
    if arr[k] != 0:
        print(k)
