```python
from itertools import permutations

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Define the find_path predicate
def find_path(start, end, path, visited):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in visited:
            new_paths = find_path(node, end, path, visited+[start])
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Define the print_all_paths predicate
def print_all_paths():
    pairs = permutations(graph.keys(), 2)
    for pair in pairs:
        paths = find_path(pair[0], pair[1], [], [])
        for path in paths:
            print(f"Path between {pair[0]} and {pair[1]}: {path}")
```