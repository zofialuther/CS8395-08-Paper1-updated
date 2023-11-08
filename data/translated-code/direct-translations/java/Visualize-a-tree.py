```python
class VisualizeTree:
    def main(self, args):
        tree = BinarySearchTree()

        tree.insert(100)
        for i in range(20):
            tree.insert(int((Math.random() * 200)))
        tree.display()

class BinarySearchTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, k):
            self.key = k
            self.left = None
            self.right = None

    def insert(self, key):
        if self.root is None:
            self.root = self.Node(key)
        else:
            n = self.root
            parent = None
            while True:
                if n.key == key:
                    return False

                parent = n

                goLeft = key < n.key
                n = n.left if goLeft else n.right

                if n is None:
                    if goLeft:
                        parent.left = self.Node(key)
                    else:
                        parent.right = self.Node(key)
                    break
        return True

    def display(self):
        height = 5
        width = 64

        len = width * height * 2 + 2
        sb = [" " for i in range(len)]
        for i in range(1, len):
            if i < len - 2 and i % width == 0:
                sb[i] = "\n"
            else:
                sb[i] = " "

        self.displayR(sb, width // 2, 1, width // 4, width, self.root, " ")
        print(''.join(sb))

    def displayR(self, sb, c, r, d, w, n, edge):
        if n:
            self.displayR(sb, c - d, r + 2, d // 2, w, n.left, " /")

            s = str(n.key)
            idx1 = r * w + c - (len(s) + 1) // 2
            idx2 = idx1 + len(s)
            idx3 = idx1 - w
            if idx2 < len(sb):
                sb[idx1:idx2] = s
                sb[idx3:idx3 + 2] = edge

            self.displayR(sb, c + d, r + 2, d // 2, w, n.right, "\\ ")
```