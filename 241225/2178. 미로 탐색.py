import heapq

def dijkstra(start):
    global graph, distance
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, curr_idx = heapq.heappop(q)
        if distance[curr_idx] < dist:
            continue
        for i in graph[curr_idx]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (distance[i[0]], i[0]))

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
distance = [[21e8] * m for _ in range(n)]
dijkstra(0)