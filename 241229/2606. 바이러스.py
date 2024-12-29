import sys
input = sys.stdin.readline

def dfs(x):
    global visited, graph
    # 현재 노드 방문
    visited[x] = 1
    for i in graph[x]:
        # 방문하지 않은 경우
        if not visited[i]:
            dfs(i)
    return

computer = int(input())
n = int(input())
graph = [[] for _ in range(computer + 1)]
for i in range(n):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0] * (computer + 1)
dfs(1)
cnt = 0
for i in visited:
    if i: cnt += 1

print(cnt - 1)