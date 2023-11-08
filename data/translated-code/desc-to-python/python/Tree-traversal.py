```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')

def levelorder(node):
    if node is None:
        return
    queue = []
    queue.append(node)
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.value, end=' ')
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

def print_tree(node):
    if node is None:
        return
    print(node.value, end=' ')
    print_tree(node.left)
    print_tree(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder Traversal:")
preorder(root)
print("\nInorder Traversal:")
inorder(root)
print("\nPostorder Traversal:")
postorder(root)
print("\nLevelorder Traversal:")
levelorder(root)
```