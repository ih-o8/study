n = int(input())
b = n // 5
while b >= 0:
    a = (n - (5 * b)) // 3
    if 3 * a + 5 * b == n:
        print(a + b)
        break
    else:
        if b == 0:
            print(-1)
            break
        b -= 1