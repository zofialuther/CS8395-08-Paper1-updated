```python
import numpy as np

def floyd_warshall(weights, num_vertices):
    dist = np.full((num_vertices, num_vertices), np.inf)
    for w in weights:
        dist[w[0] - 1][w[1] - 1] = w[2]

    next = np.zeros((num_vertices, num_vertices), dtype=int)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:
                next[i][j] = j + 1

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    print_result(dist, next)

def print_result(dist, next):
    print("pair     dist    path")
    for i in range(len(next)):
        for j in range(len(next)):
            if i != j:
                u = i + 1
                v = j + 1
                path = f"{u} -> {v}    {int(dist[i][j])}     {u}"
                while u != v:
                    u = next[u - 1][v - 1]
                    path += f" -> {u}"
                print(path)

weights = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]
num_vertices = 4

floyd_warshall(weights, num_vertices)
```