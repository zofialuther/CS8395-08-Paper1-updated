class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def visit(self):
        print(self.value, end=" ")

def traverse(node, order):
    if node is None:
        return
    if order == "PREORDER":
        node.visit()
        traverse(node.left, order)
        traverse(node.right, order)
    elif order == "INORDER":
        traverse(node.left, order)
        node.visit()
        traverse(node.right, order)
    elif order == "POSTORDER":
        traverse(node.left, order)
        traverse(node.right, order)
        node.visit()
    elif order == "LEVEL":
        queue = []
        queue.append(node)
        while queue:
            next_node = queue.pop(0)
            next_node.visit()
            if next_node.left:
                queue.append(next_node.left)
            if next_node.right:
                queue.append(next_node.right)

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
four.left = seven
six.left = eight
six.right = nine

traverse(one, "PREORDER")
print()
traverse(one, "INORDER")
print()
traverse(one, "POSTORDER")
print()
traverse(one, "LEVEL")