import heapq

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

map = [[21e8] * m for _ in range(n)]

heap = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            start_x, start_y = i, j
        elif arr[i][j] == 'X':
