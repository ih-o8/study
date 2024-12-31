n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

print(graph)

visi
for i in range(1, n + 1):
