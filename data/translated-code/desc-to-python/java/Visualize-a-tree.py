class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursively(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursively(current.right, value)

    def display(self):
        self._display_recursively(self.root, 0)

    def _display_recursively(self, node, level):
        if node is not None:
            self._display_recursively(node.right, level+1)
            print(' ' * 4 * level + '->', node.value)
            self._display_recursively(node.left, level+1)

# Main method
tree = BinarySearchTree()
for _ in range(20):
    value = random.randint(1, 100)
    tree.insert(value)
tree.display()