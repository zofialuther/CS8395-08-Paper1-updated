```python
import queue

class HuffmanTree:
    def __init__(self, freq):
        self.frequency = freq

    def __lt__(self, tree):
        return self.frequency < tree.frequency

class HuffmanLeaf(HuffmanTree):
    def __init__(self, freq, val):
        super().__init__(freq)
        self.value = val

class HuffmanNode(HuffmanTree):
    def __init__(self, l, r):
        super().__init__(l.frequency + r.frequency)
        self.left = l
        self.right = r

def buildTree(charFreqs):
    trees = queue.PriorityQueue()
    for i in range(len(charFreqs)):
        if charFreqs[i] > 0:
            trees.put(HuffmanLeaf(charFreqs[i], chr(i)))

    assert trees.qsize() > 0
    while trees.qsize() > 1:
        a = trees.get()
        b = trees.get()
        trees.put(HuffmanNode(a, b))
    return trees.get()

def printCodes(tree, prefix):
    if isinstance(tree, HuffmanLeaf):
        leaf = tree
        print(leaf.value, "\t", leaf.frequency, "\t", prefix)

    elif isinstance(tree, HuffmanNode):
        node = tree
        printCodes(node.left, prefix + '0')
        printCodes(node.right, prefix + '1')

def main():
    test = "this is an example for huffman encoding"
    charFreqs = [0] * 256
    for c in test:
        charFreqs[ord(c)] += 1

    tree = buildTree(charFreqs)
    print("SYMBOL\tWEIGHT\tHUFFMAN CODE")
    printCodes(tree, "")

if __name__ == "__main__":
    main()
```