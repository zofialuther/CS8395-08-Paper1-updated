```python
def preorder(tree):
    if tree:
        print(tree[0], end=" ")
        preorder(tree[1])
        preorder(tree[2])

def inorder(tree):
    if tree:
        inorder(tree[1])
        print(tree[0], end=" ")
        inorder(tree[2])

def postorder(tree):
    if tree:
        postorder(tree[1])
        postorder(tree[2])
        print(tree[0], end=" ")

def level_order(tree):
    queue = [tree]
    while queue:
        node = queue.pop(0)
        if node:
            print(node[0], end=" ")
            if node[1]:
                queue.append(node[1])
            if node[2]:
                queue.append(node[2])

tree = [1,
        [2,
         [4,
          [7, None, None],
          None],
         [5, None, None]],
        [3,
         [6,
          [8, None, None],
          [9,None, None]],
         None]]

print('preorder    : ', end="")
preorder(tree)
print()
print('inorder     : ', end="")
inorder(tree)
print()
print('postorder   : ', end="")
postorder(tree)
print()
print('level-order : ', end="")
level_order(tree)
```