class Dijkstra:
    GRAPH = [Edge('A', 'B', 3), Edge('B', 'C', 4), Edge('A', 'C', 7)]
    START = 'A'
    END = 'C'

    def main(self):
        graph = Graph(self.GRAPH)
        graph.dijkstra()
        print(graph.printPath(self.START, self.END))

class Graph:
    def __init__(self, edges):
        self.graph = {}
        for edge in edges:
            if edge.v1 not in self.graph:
                self.graph[edge.v1] = Vertex(edge.v1)
            if edge.v2 not in self.graph:
                self.graph[edge.v2] = Vertex(edge.v2)
            self.graph[edge.v1].neighbours[edge.v2] = edge.dist
            self.graph[edge.v2].neighbours[edge.v1] = edge.dist

    def dijkstra(self):
        # implementation of Dijkstra's algorithm using a binary heap
        pass

    def printPath(self, start, end):
        # implementation of printing the path
        pass

class Edge:
    def __init__(self, v1, v2, dist):
        self.v1 = v1
        self.v2 = v2
        self.dist = dist

class Vertex:
    def __init__(self, name):
        self.name = name
        self.dist = float('inf')
        self.previous = None
        self.neighbours = {}