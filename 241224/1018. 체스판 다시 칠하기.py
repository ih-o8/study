n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
ans = 64

for i in range(n-7):
    for j in range(m-7):
        wb_cnt = 0
        bw_cnt = 0
        for x in range(8):
            for y in range(8):
                # 짝수 번째 열(0,2,4,6)
                if (i+x) % 2 == 0:
                    # 짝수 번째 행
                    if (j+y) % 2 == 0:
                        if arr[i+x][j+y] != 'B':
                            wb_cnt += 1
                        else:
                            bw_cnt += 1
                    # 홀수 번째 행
                    else:
                        if arr[i+x][j+y] != 'W':
                            wb_cnt += 1
                        else:
                            bw_cnt += 1
                # 홀수 번째 열(1,3,5,7)
                else:
                    # 짝수 번째 행
                    if (j + y) % 2 == 0:
                        if arr[i + x][j + y] != 'W':
                            wb_cnt += 1
                        else:
                            bw_cnt += 1
                    # 홀수 번째 행
                    else:
                        if arr[i + x][j + y] != 'B':
                            wb_cnt += 1
                        else:
                            bw_cnt += 1

        if ans > wb_cnt:
            ans = wb_cnt
        if ans > bw_cnt:
            ans = bw_cnt

print(ans)
