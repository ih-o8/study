# BFS
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
visited = [[21e8] * m for _ in range(n)]
queue = deque([(1, 0, 0)])

while queue:
    cnt, x, y = queue.popleft()
    if visited[x][y] > cnt:
        visited[x][y] = cnt
        for i in range(4):
            ni = x + direction[i][0]
            nj = y + direction[i][1]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj]:
                queue.append((cnt + 1, ni, nj))

print(visited[n - 1][m - 1])
