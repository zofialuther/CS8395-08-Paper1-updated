class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def visit(self):
    print(str(self.value) + " ")

from enum import Enum
class ORDER(Enum):
  PREORDER = 1
  INORDER = 2
  POSTORDER = 3
  LEVEL = 4

def traverse(node, order):
  if node is None:
    return
  if order == ORDER.PREORDER:
    node.visit()
    traverse(node.left, order)
    traverse(node.right, order)
  elif order == ORDER.INORDER:
    traverse(node.left, order)
    node.visit()
    traverse(node.right, order)
  elif order == ORDER.POSTORDER:
    traverse(node.left, order)
    traverse(node.right, order)
    node.visit()
  elif order == ORDER.LEVEL:
    queue = [node]
    while queue:
      next = queue.pop(0)
      next.visit()
      if next.left:
        queue.append(next.left)
      if next.right:
        queue.append(next.right)

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

traverse(one, ORDER.PREORDER)
print("\n")
traverse(one, ORDER.INORDER)
print("\n")
traverse(one, ORDER.POSTORDER)
print("\n")
traverse(one, ORDER.LEVEL)