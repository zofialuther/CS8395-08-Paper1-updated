```python
# Python code to define a tree data structure and provide functions to traverse the tree in different orders
# The tree is represented as a list where each element is a node with its left and right children

# Function to perform preorder traversal of the tree
def preorder_traversal(tree):
    if tree:
        print(tree[0])
        preorder_traversal(tree[1])
        preorder_traversal(tree[2])

# Function to perform inorder traversal of the tree
def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree[1])
        print(tree[0])
        inorder_traversal(tree[2])

# Function to perform postorder traversal of the tree
def postorder_traversal(tree):
    if tree:
        postorder_traversal(tree[1])
        postorder_traversal(tree[2])
        print(tree[0])

# Function to perform level-order traversal of the tree
def level_order_traversal(tree):
    if not tree:
        return
    queue = [tree]
    while queue:
        node = queue.pop(0)
        print(node[0])
        if node[1]:
            queue.append(node[1])
        if node[2]:
            queue.append(node[2])

# Example usage
tree = [1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], [7, None, None]]]
print("Preorder traversal:")
preorder_traversal(tree)
print("Inorder traversal:")
inorder_traversal(tree)
print("Postorder traversal:")
postorder_traversal(tree)
print("Level-order traversal:")
level_order_traversal(tree)
```