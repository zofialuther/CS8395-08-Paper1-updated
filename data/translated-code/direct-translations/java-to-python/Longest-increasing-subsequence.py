from typing import List
import bisect

class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None

    def __lt__(self, other):
        return self.value < other.value

def lis(n: List[int]) -> List[int]:
    pileTops = []
    for x in n:
        node = Node(x)
        i = bisect.bisect_left(pileTops, node)
        if i != 0:
            node.pointer = pileTops[i-1]
        if i != len(pileTops):
            pileTops[i] = node
        else:
            pileTops.append(node)
    
    result = []
    node = pileTops[-1] if pileTops else None
    while node:
        result.append(node.value)
        node = node.pointer
    result.reverse()
    return result

if __name__ == "__main__":
    d = [3,2,6,4,5,1]
    print(f"an L.I.S. of {d} is {lis(d)}")
    d = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(f"an L.I.S. of {d} is {lis(d)}")