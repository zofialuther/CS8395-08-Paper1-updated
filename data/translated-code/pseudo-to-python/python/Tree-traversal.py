```python
def printwithspace(i):
    print("%i " % i, end='')

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def preorder(self, visitor):
        if self is not None:
            visitor(self.data)
            Node.preorder(self.left, visitor)
            Node.preorder(self.right, visitor)

    def inorder(self, visitor):
        if self is not None:
            Node.inorder(self.left, visitor)
            visitor(self.data)
            Node.inorder(self.right, visitor)

    def postorder(self, visitor):
        if self is not None:
            Node.postorder(self.left, visitor)
            Node.postorder(self.right, visitor)
            visitor(self.data)

    def levelorder(self, visitor, more=None):
        if self is not None:
            if more is None:
                more = []
            more += [self.left, self.right]
            visitor(self.data)
        if more:
            Node.levelorder(more[0], visitor, more[1:])

tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))

if __name__ == '__main__':
    print('  preorder: ', end='')
    tree.preorder(printwithspace)
    print('\n   inorder: ', end='')
    tree.inorder(printwithspace)
    print('\n postorder: ', end='')
    tree.postorder(printwithspace)
    print('\nlevelorder: ', end='')
    tree.levelorder(printwithspace)
    print('\n')
```