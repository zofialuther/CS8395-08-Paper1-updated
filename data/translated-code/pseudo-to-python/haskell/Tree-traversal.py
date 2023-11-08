class Node:
  def __init__(self, value, left, right):
    self.value = value
    self.left = left
    self.right = right

def preorder(node):
  if node is None:
    return []
  else:
    return [node.value] + preorder(node.left) + preorder(node.right)

def inorder(node):
  if node is None:
    return []
  else:
    return inorder(node.left) + [node.value] + inorder(node.right)

def postorder(node):
  if node is None:
    return []
  else:
    return postorder(node.left) + postorder(node.right) + [node.value]

def levelorder(node):
  queue = [node]
  result = []
  while queue:
    current = queue.pop(0)
    if current is not None:
      result.append(current.value)
      queue.append(current.left)
      queue.append(current.right)
  return result

tree = Node(1, Node(2, Node(4, Node(7, None, None), None), Node(5, None, None)), Node(3, Node(6, Node(8, None, None), Node(9, None, None), None)))

asciiTree = "         1\n        / \\\n       /   \\\n      /     \\\n     2       3\n    / \\     /\n   4   5   6\n  /       / \\\n 7       8   9"

def main():
  print(asciiTree)
  for i in range(4):
    traversal = [preorder, inorder, postorder, levelorder][i](tree)
    print(justifyLeft(14, ' ', ["preorder", "inorder", "postorder", "level-order"][i] + ":") + ' '.join(map(str, traversal)))

def justifyLeft(n, c, s):
  return s.ljust(n, c)

main()