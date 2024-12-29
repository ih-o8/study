# # BFS
#
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# def find_start():
#     global n, m, arr
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 2:
#                 return (i, j)
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# x, y = find_start()
#
# ans = [[21e8] * m for _ in range(n)]
# direction = [(-1, 0),(1, 0), (0, -1), (0, 1)]
#
# queue = deque([(x, y, 0)]) # x, y, 합계
# ans[x][y] = 0
#
# while queue:
#     di, dj, num = queue.popleft()
#     for i in range(4):
#         ni = di + direction[i][0]
#         nj = dj + direction[i][1]
#         if 0 <= ni < n and 0 <= nj < m:
#             if arr[ni][nj] == 1:
#                 if ans[ni][nj] > num + 1:
#                     ans[ni][nj] = num + 1
#                     queue.append((ni, nj, num + 1))
#             if arr[ni][nj] == 0:
#                 ans[ni][nj] = 0
#
# for j in range(n):
#     for k in range(m):
#         if ans[j][k] == 21e8:
#             if arr[j][k] == 0:
#                 ans[j][k] = 0
#             else:
#                 ans[j][k] = -1
#     print(*ans[j])


# 효율적으로 코드 보완(시간 단축 800ms => 672ms)
# BFS

import sys
from collections import deque
input = sys.stdin.readline

def find_start():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return (i, j)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y = find_start()

ans = [[-1] * m for _ in range(n)]
direction = [(-1, 0),(1, 0), (0, -1), (0, 1)]

queue = deque([(x, y)])
ans[x][y] = 0

while queue:
    di, dj = queue.popleft()
    for i, j in direction:
        ni, nj = di + i, dj + j
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] == 1 and ans[ni][nj] == -1:
                ans[ni][nj] = ans[di][dj] + 1
                queue.append((ni, nj))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans[i][j] = 0
    print(*ans[i])