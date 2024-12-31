while True:
    a, b, c = input().split()
    if a == c == '0' and b == 'W':
        break
    if b == 'W':
        ans = int(a) - int(c)
    else:
        ans = int(a) + int(c)

    if ans < -200:
        print('Not allowed')
    else:
        print(ans)