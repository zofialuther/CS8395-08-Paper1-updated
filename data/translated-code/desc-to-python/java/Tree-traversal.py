```python
class TreeTraversal:
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    class ORDER(Enum):
        PREORDER = 1
        INORDER = 2
        POSTORDER = 3
        LEVEL = 4
    
    def __init__(self):
        pass
    
    def traverse(self, root, order):
        if order == self.ORDER.PREORDER:
            self.preorder(root)
        elif order == self.ORDER.INORDER:
            self.inorder(root)
        elif order == self.ORDER.POSTORDER:
            self.postorder(root)
        elif order == self.ORDER.LEVEL:
            self.levelorder(root)
    
    def preorder(self, node):
        if node is not None:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
    
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)
    
    def levelorder(self, root):
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```