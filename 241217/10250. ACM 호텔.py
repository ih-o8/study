for _ in range(int(input())):
    h, w, n = map(int, input().split())
    # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님

    if n % h == 0:
        floor = h
        room = n // h
    else:
        floor = n % h
        room = n // h + 1

    if room < 10:
        print(f'{floor}0{room}')
    else:
        print(f'{floor}{room}')
