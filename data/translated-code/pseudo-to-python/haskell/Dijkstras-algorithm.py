```python
import math

def dijkstra(source, target, adj_list):
    min_distance = [math.inf] * len(adj_list)
    min_distance[source] = 0
    previous = [-1] * len(adj_list)
    
    def aux(vertex_queue):
        if not vertex_queue:
            return
        vertex = min(vertex_queue, key=lambda v: min_distance[v])
        vertex_queue.remove(vertex)
        for edge in adj_list[vertex]:
            u, v, weight = edge
            new_distance = min_distance[vertex] + weight
            if new_distance < min_distance[v]:
                min_distance[v] = new_distance
                previous[v] = vertex
                vertex_queue.append(v)
        aux(vertex_queue)
    
    aux([source])
    return (tuple(min_distance), tuple(previous))

def shortest_path_to(target, previous):
    def find_path(vertex, path):
        if vertex == -1:
            return path
        path.append(vertex)
        return find_path(previous[vertex], path)
    
    return find_path(target, [])[::-1]

adj_list = [
    [(1, 2, 7), (2, 3, 9)],
    [(0, 2, 7), (2, 4, 3), (3, 5, 4)],
    [(0, 3, 9), (1, 4, 6), (4, 5, 2)],
    [(1, 5, 4), (4, 6, 5)],
    [(2, 5, 2), (1, 3, 3), (2, 5, 2), (3, 6, 5)],
    [(3, 6, 5), (4, 5, 2), (2, 4, 2)]
]

def main():
    distance, previous = dijkstra(0, -1, adj_list)
    print(f"Distance from source to target: {distance[5]}")
    path = shortest_path_to(5, previous)
    print(f"Shortest path to target: {path}")

main()
```