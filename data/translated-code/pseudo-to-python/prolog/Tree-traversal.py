Tree = [1,
        [2,
            [4,
                [7, None, None],
                None,
            ],
            [5, None, None],
        ],
        [3,
            [6,
                [8, None, None],
                [9, None, None],
            ],
            None,
        ],
    ]

def preorder(tree):
    if tree is None:
        return
    print(tree[0], end=" ")
    preorder(tree[1])
    preorder(tree[2])

def inorder(tree):
    if tree is None:
        return
    inorder(tree[1])
    print(tree[0], end=" ")
    inorder(tree[2])

def postorder(tree):
    if tree is None:
        return
    postorder(tree[1])
    postorder(tree[2])
    print(tree[0], end=" ")

def level_order(tree):
    if not tree:
        return
    queue = [tree[0]]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        if node[1]:
            queue.append(node[1])
        if node[2]:
            queue.append(node[2])

print('preorder    : ', end="")
preorder(Tree)
print()
print('inorder     : ', end="")
inorder(Tree)
print()
print('postorder   : ', end="")
postorder(Tree)
print()
print('level-order : ', end="")
level_order([Tree])