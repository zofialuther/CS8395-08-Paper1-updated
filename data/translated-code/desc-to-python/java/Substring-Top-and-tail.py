```python
def remove_chars(string):
    return string[1:-1]

def remove_chars_regex(string):
    import re
    return re.sub(r'^.|.$', '', string)

words = ["knight", "socks", "brooms"]

for word in words:
    print("Original:", word)
    print("Method 1:", remove_chars(word))
    print("Method 2:", remove_chars_regex(word))
```