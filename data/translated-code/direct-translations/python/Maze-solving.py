```python
def Dijkstra(Graph, source):
    infinity = float('inf')
    n = len(Graph)
    dist = [infinity]*n
    previous = [infinity]*n
    dist[source] = 0
    Q = list(range(n))
    while Q:
        u = min(Q, key=lambda n:dist[n])
        Q.remove(u)
        if dist[u] == infinity:
            break
        for v in range(n):
            if Graph[u][v] and (v in Q):
                alt = dist[u] + Graph[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
    return dist, previous

def display_solution(predecessor):
    cell = len(predecessor)-1
    while cell:
        print(cell, end='<')
        cell = predecessor[cell]
    print(0)
```