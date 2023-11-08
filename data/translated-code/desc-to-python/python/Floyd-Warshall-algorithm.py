```python
import sys

def floydWarshall(graph, V):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    print("Shortest distances between all pairs of vertices:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == sys.maxsize:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print("")

# Example input
V = 4
graph = [[0, 5, sys.maxsize, 10],
         [sys.maxsize, 0, 3, sys.maxsize],
         [sys.maxsize, sys.maxsize, 0, 1],
         [sys.maxsize, sys.maxsize, sys.maxsize, 0]]

floydWarshall(graph, V)
```