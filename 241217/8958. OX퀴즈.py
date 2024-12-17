for _ in range(int(input())):
    score = input()
    cnt = 1
    ans = 0
    for i in score:
        if i == 'O':
            ans += cnt
            cnt += 1
        else:
            cnt = 1
    print(ans)