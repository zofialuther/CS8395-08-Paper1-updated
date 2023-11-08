```python
import collections
import heapq
import pprint

class Graph:
    def __init__(self):
        self.edges = collections.defaultdict(list)
        self.cost = {}

    def add_edge(self, u, v, w):
        self.edges[u].append(v)
        self.edges[v].append(u)
        self.cost[(u, v)] = w
        self.cost[(v, u)] = w

    def dijkstra(self, source, dest):
        queue = [(0, source, ())]
        visited = set()
        dist = {source: 0}
        while queue:
            (cost, current, path) = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            path += (current,)
            if current == dest:
                return (cost, path)
            for neighbor in self.edges[current]:
                if neighbor in visited:
                    continue
                new_cost = cost + self.cost[(current, neighbor)]
                if neighbor not in dist or new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor, path))
        return float("inf"), []

g = Graph()
g.add_edge("A", "B", 1)
g.add_edge("A", "C", 4)
g.add_edge("B", "C", 2)
g.add_edge("B", "D", 5)
g.add_edge("C", "D", 1)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(g.dijkstra("A", "D"))
```