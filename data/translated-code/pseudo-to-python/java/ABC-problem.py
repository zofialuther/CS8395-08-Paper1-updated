class ABC:
    def main(self):
        blocks = ["abc", "def", "ghi"]
        words = ["apple", "banana", "orange"]
        for word in words:
            print(word, self.canMakeWord(word, blocks))

    def canMakeWord(self, word, blocks):
        if word == "":
            return True
        first_char = word[0]
        for i in range(len(blocks)):
            if blocks[i][0] == first_char or blocks[i][1] == first_char:
                blocks[i], blocks[0] = blocks[0], blocks[i]
                if self.canMakeWord(word[1:], blocks[1:]):
                    return True
                blocks[i], blocks[0] = blocks[0], blocks[i]
        return False