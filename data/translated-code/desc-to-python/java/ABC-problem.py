```python
def canMakeWord(blocks, word):
    if len(word) == 0:
        return True
    for i in range(len(blocks)):
        if word[0] in blocks[i]:
            new_blocks = blocks[:i] + blocks[i+1:]
            if canMakeWord(new_blocks, word[1:]):
                return True
    return False

def main():
    letter_blocks = ["abc", "def", "ghi"]
    words = ["bad", "fed", "had", "dig"]
    for word in words:
        if canMakeWord(letter_blocks, word):
            print(word + " can be formed using the given letter blocks")
        else:
            print(word + " cannot be formed using the given letter blocks")

main()
```