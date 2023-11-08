```python
class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def preorder(tree):
    if tree is None:
        return []
    return [tree.value] + preorder(tree.left) + preorder(tree.right)

def inorder(tree):
    if tree is None:
        return []
    return inorder(tree.left) + [tree.value] + inorder(tree.right)

def postorder(tree):
    if tree is None:
        return []
    return postorder(tree.left) + postorder(tree.right) + [tree.value]

def levelorder(tree):
    if tree is None:
        return []
    result = []
    queue = [tree]
    while queue:
        node = queue.pop(0)
        if node is not None:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
    return result

tree = Tree(1, Tree(2, Tree(4, Tree(7, None, None), None), Tree(5, None, None)), Tree(3, Tree(6, Tree(8, None, None), Tree(9, None, None)), None))

def justifyLeft(n, c, s):
    return (s + c * n)[:n]

asciiTree = '''
         1
        / \\
       /   \\
      /     \\
     2       3
    / \\     /
   4   5   6
  /       / \\
 7       8   9
'''

print(asciiTree)
for s, xs in zip(["preorder", "inorder", "postorder", "level-order"], [preorder(tree), inorder(tree), postorder(tree), levelorder(tree)]):
    print(justifyLeft(14, ' ', s + ":"), ' '.join(map(str, xs)))
```