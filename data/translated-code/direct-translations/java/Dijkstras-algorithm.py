class Dijkstra:
    GRAPH = [
        ("a", "b", 7),
        ("a", "c", 9),
        ("a", "f", 14),
        ("b", "c", 10),
        ("b", "d", 15),
        ("c", "d", 11),
        ("c", "f", 2),
        ("d", "e", 6),
        ("e", "f", 9)
    ]
    START = "a"
    END = "e"

    def main(self):
        g = Graph(self.GRAPH)
        g.dijkstra(self.START)
        g.printPath(self.END)
        # g.printAllPaths()


class Graph:
    def __init__(self, edges):
        self.graph = {}
        for e in edges:
            if e[0] not in self.graph:
                self.graph[e[0]] = Vertex(e[0])
            if e[1] not in self.graph:
                self.graph[e[1]] = Vertex(e[1])
        
        for e in edges:
            self.graph[e[0]].neighbours[self.graph[e[1]]] = e[2]

    def dijkstra(self, start_name):
        if start_name not in self.graph:
            print(f"Graph doesn't contain start vertex \"{start_name}\"")
            return
        source = self.graph[start_name]
        q = []
        for v in self.graph.values():
            v.previous = v if v == source else None
            v.dist = 0 if v == source else float('inf')
            q.append(v)
        self._dijkstra(q)

    def _dijkstra(self, q):
        while q:
            u = min(q, key=lambda v: v.dist)
            q.remove(u)
            for v, dist in u.neighbours.items():
                alt_dist = u.dist + dist
                if alt_dist < v.dist:
                    v.dist = alt_dist
                    v.previous = u
    
    def printPath(self, end_name):
        if end_name not in self.graph:
            print(f"Graph doesn't contain end vertex \"{end_name}\"")
            return
        self.graph[end_name].printPath()


class Vertex:
    def __init__(self, name):
        self.name = name
        self.dist = float('inf')
        self.previous = None
        self.neighbours = {}

    def printPath(self):
        if self.previous == self:
            print(f"{self.name}")
        elif self.previous is None:
            print(f"{self.name}(unreached)")
        else:
            self.previous.printPath()
            print(f" -> {self.name}({self.dist})")