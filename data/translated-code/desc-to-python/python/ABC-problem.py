```python
# The code is not functioning correctly for certain cases

def can_make_word(word, blocks):
    blocks = [set(pair) for pair in blocks]
    word = word.upper()
    for letter in word:
        matching_block = None
        for block in blocks:
            if letter in block:
                matching_block = block
                break
        if matching_block:
            blocks.remove(matching_block)
        else:
            return False
    return True

# Test cases
print(can_make_word("hello", ["eo", "lL", "hH"]))  # False
print(can_make_word("hello", ["eo", "lL", "hH", "lo"]))  # True
print(can_make_word("world", ["wo", "rl", "d"]))  # True
print(can_make_word("python", ["py", "th", "on"]))  # False
```