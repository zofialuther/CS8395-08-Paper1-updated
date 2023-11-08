from anytree import Node, RenderTree

tree = Node("1")
node2 = Node("2", parent=tree)
node3 = Node("3", parent=tree)
node4 = Node("4", parent=node2)
node5 = Node("5", parent=node2)
node6 = Node("6", parent=node3)
node7 = Node("7", parent=node4)
node8 = Node("8", parent=node6)
node9 = Node("9", parent=node6)

for pre, fill, node in RenderTree(tree):
    print("%s%s" % (pre, node.name))