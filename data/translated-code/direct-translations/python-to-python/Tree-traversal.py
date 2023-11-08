from collections import namedtuple
import sys

class Node(namedtuple('Node', 'data, left, right')):
    __slots__ = ()

    def preorder(self, visitor):
        if self is not None:
            visitor(self.data)
            if self.left:
                self.left.preorder(visitor)
            if self.right:
                self.right.preorder(visitor)

    def inorder(self, visitor):
        if self is not None:
            if self.left:
                self.left.inorder(visitor)
            visitor(self.data)
            if self.right:
                self.right.inorder(visitor)

    def postorder(self, visitor):
        if self is not None:
            if self.left:
                self.left.postorder(visitor)
            if self.right:
                self.right.postorder(visitor)
            visitor(self.data)

    def levelorder(self, visitor):
        nodes = [self]
        while nodes:
            current = nodes.pop(0)
            if current:
                visitor(current.data)
                if current.left:
                    nodes.append(current.left)
                if current.right:
                    nodes.append(current.right)


def printwithspace(i):
    sys.stdout.write("%i " % i)


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
    sys.stdout.write('  preorder: ')
    tree.preorder(printwithspace)
    sys.stdout.write('\n   inorder: ')
    tree.inorder(printwithspace)
    sys.stdout.write('\n postorder: ')
    tree.postorder(printwithspace)
    sys.stdout.write('\nlevelorder: ')
    tree.levelorder(printwithspace)
    sys.stdout.write('\n')