```python
import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, start, end, weight):
        if start not in self.edges:
            self.edges[start] = []
        self.edges[start].append((end, weight))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.edges}
        distances[start] = 0
        queue = [(0, start)]
        
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        return distances

    def shortest_path(self, start, end):
        distances = self.dijkstra(start)
        path = []
        current_vertex = end
        while current_vertex != start:
            path.insert(0, current_vertex)
            for neighbor, weight in self.edges[current_vertex]:
                if distances[current_vertex] == distances[neighbor] + weight:
                    current_vertex = neighbor
                    break
        path.insert(0, start)
        return path

# Main method
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)

    start_vertex = 'A'
    end_vertex = 'D'
    shortest_path = graph.shortest_path(start_vertex, end_vertex)
    print(f"The shortest path from {start_vertex} to {end_vertex} is {shortest_path}")
```