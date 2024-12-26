# BFS
import sys
input = sys.stdin.readline
from collections import deque

def find_start(n, m):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'I':
                start = (i, j)
                return start

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
queue = deque([find_start(n, m)])
visited = [[0] * m for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
ans = 0

while queue:
    x, y = queue.popleft()
    if not visited[x][y]:
        visited[x][y] = 1  # 방문 표시
        if arr[x][y] == 'P':
            ans += 1  # 사람 발견 시 +1
        for i in range(4):
            ni = x + direction[i][0]
            nj = y + direction[i][1]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] != 'X':
                    queue.append((ni, nj))

if ans:
    print(ans)
else:
    print('TT')


print(arr)