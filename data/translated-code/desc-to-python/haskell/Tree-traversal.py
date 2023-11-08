```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

    def preorder(self, node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

    def levelorder(self, node):
        if node is None:
            return
        queue = [node]
        while queue:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    tree = Tree(root)

    print("Preorder traversal:")
    tree.preorder(root)

    print("Inorder traversal:")
    tree.inorder(root)

    print("Postorder traversal:")
    tree.postorder(root)

    print("Levelorder traversal:")
    tree.levelorder(root)

if __name__ == "__main__":
    main()
```