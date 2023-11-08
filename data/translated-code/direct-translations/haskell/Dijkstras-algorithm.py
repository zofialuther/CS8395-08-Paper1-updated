from typing import List, Tuple
from array import array

def dijkstra(src: str, invalid_index: str, adj_list: array) -> Tuple[array, array]:
    def newSTArray(bounds: Tuple, e: int):
        return array('i', [e for _ in range(bounds[0], bounds[1]+1)])

    def shortest_path_to(target: str, invalid_index: str, previous: array) -> List:
        vertex = target
        acc = []
        while vertex != invalid_index:
            acc.append(vertex)
            vertex = previous[ord(vertex)-ord('a')]
        return acc

    b = adj_list.bounds
    min_distance = newSTArray(b, float('inf'))
    min_distance[ord(src)-ord('a')] = 0
    previous = newSTArray(b, ord(invalid_index))
    vertex_queue = set([(0, src)])

    while vertex_queue:
        (dist, u), vertex_queue = vertex_queue.pop()
        edges = adj_list[ord(u)-ord('a')]
        for v, weight in edges:
            dist_thru_u = dist + weight
            if dist_thru_u < min_distance[ord(v)-ord('a')]:
                vertex_queue.discard((min_distance[ord(v)-ord('a')], v))
                min_distance[ord(v)-ord('a')] = dist_thru_u
                previous[ord(v)-ord('a')] = ord(u)

                vertex_queue.add((dist_thru_u, v))

    return min_distance, previous


adj_list = array('i', [ [('b',7), ('c',9), ('f',14)],
                        [('a',7), ('c',10), ('d',15)],
                        [('a',9), ('b',10), ('d',11), ('f',2)],
                        [('b',15), ('c',11), ('e',6)],
                        [('d',6), ('f',9)],
                        [('a',14), ('c',2), ('e',9)] ])

min_distance, previous = dijkstra('a', ' ', adj_list)
print("Distance from a to e:", min_distance[ord('e')-ord('a')])
path = shortest_path_to('e', ' ', previous)
print("Path:", path)