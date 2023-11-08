class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None

def lis(input_list):
    pileTops = []
    for x in input_list:
        node = Node(x)
        i = bisect_left(pileTops, node)
        if i < 0:
            i = ~i
        if i != 0:
            node.pointer = pileTops[i-1]
        if i != len(pileTops):
            pileTops[i] = node
        else:
            pileTops.append(node)
    result = []
    for node in reversed(pileTops):
        result.append(node.value)
    return result

d = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(d)
print(lis(d))

d2 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(d2)
print(lis(d2))