```python
import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

def display_path(predecessors, source, target):
    path = []
    while target:
        path.insert(0, target)
        target = predecessors[target]
    if path[0] == source:
        print('Optimal path:', ' -> '.join(path))
    else:
        print('No path found from', source, 'to', path[-1])

# Sample graph
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 2},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 2},
    'D': {'B': 2, 'C': 4, 'E': 1},
    'E': {'C': 2, 'D': 1}
}

source_node = 'A'
shortest_distances = dijkstra(graph, source_node)
print('Shortest distances:', shortest_distances)
display_path({'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'C'}, source_node, 'E')
```