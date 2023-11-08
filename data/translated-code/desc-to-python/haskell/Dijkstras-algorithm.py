```python
import heapq

def dijkstra(s, invalid, graph):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [invalid] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

def shortest_path_to(s, t, prev):
    path = []
    while t != s:
        path.append(t)
        t = prev[t]
    path.append(s)
    return list(reversed(path))

graph = [
    [(1, 4), (2, 2)],
    [(3, 2)],
    [(1, 1), (3, 5)],
    [(4, 3)],
    []
]

invalid = -1
source = 0
target = 4

distances, previous = dijkstra(source, invalid, graph)
shortest_path = shortest_path_to(source, target, previous)
print("Shortest distance:", distances[target])
print("Shortest path:", shortest_path)
```