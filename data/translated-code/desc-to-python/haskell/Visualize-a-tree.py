from Data.Tree import drawTree

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def main():
    root = Node(1)
    root.children.append(Node(2))
    root.children.append(Node(3))
    root.children[0].children.append(Node(4))
    root.children[0].children.append(Node(5))
    print(drawTree(root))