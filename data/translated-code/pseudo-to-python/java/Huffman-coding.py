class HuffmanTree:
    def __init__(self, frequency):
        self.frequency = frequency

    def compareTo(self, other):
        return self.frequency - other.frequency

class HuffmanLeaf(HuffmanTree):
    def __init__(self, frequency, value):
        super().__init__(frequency)
        self.value = value

class HuffmanNode(HuffmanTree):
    def __init__(self, frequency, left, right):
        super().__init__(frequency)
        self.left = left
        self.right = right

class HuffmanCode:
    @staticmethod
    def buildTree(frequencies):
        queue = PriorityQueue()
        for char, freq in enumerate(frequencies):
            if freq > 0:
                queue.put(HuffmanLeaf(freq, char))

        while queue.qsize() > 1:
            left = queue.get()
            right = queue.get()
            new_tree = HuffmanNode(left.frequency + right.frequency, left, right)
            queue.put(new_tree)

        return queue.get()

    @staticmethod
    def printCodes(tree, stringBuffer):
        if isinstance(tree, HuffmanLeaf):
            stringBuffer.append(str(tree.value) + ": " + str(tree.frequency) + ", " + str(stringBuffer))
        else:
            HuffmanCode.printCodes(tree.left, stringBuffer.append('0'))
            HuffmanCode.printCodes(tree.right, stringBuffer.append('1'))

    def main():
        test_string = "test string"
        frequencies = [0] * 256
        for char in test_string:
            frequencies[ord(char)] += 1

        tree = HuffmanCode.buildTree(frequencies)
        stringBuffer = []
        HuffmanCode.printCodes(tree, stringBuffer)