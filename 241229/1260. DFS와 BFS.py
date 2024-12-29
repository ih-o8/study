import sys
input = sys.stdin.readline
from collections import deque

def dfs(x):
    global visited_dfs, ans_dfs, graph
    # 방문 표시
    visited_dfs[x] = 1
    ans_dfs.append(x)
    # 방문하지 않은 곳 찾기
    for i in graph[x]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(x):
    global visited_bfs, queue, graph
    while queue:
        i = queue.popleft()
        if not visited_bfs[i]:
            ans_bfs.append(i)
            visited_bfs[i] = 1
            for j in graph[i]:
                queue.append(j)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [0] * (n + 1)
ans_dfs = []

dfs(v)
print(*ans_dfs)

visited_bfs = [0] * (n + 1)
queue = deque([v])
ans_bfs = []
bfs(v)
print(*ans_bfs)