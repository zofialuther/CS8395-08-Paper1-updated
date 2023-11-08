from Data.Tree import *

tree = Node(1, [Node(2, [Node(4, []), Node(5, [])]), Node(3, [Node(6, [])])])

def main() -> IO():
    tree_str = drawTree(fmap(str, tree))
    putStrLn(tree_str)