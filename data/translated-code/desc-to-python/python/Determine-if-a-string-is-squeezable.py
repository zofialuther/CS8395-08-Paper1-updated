```python
from itertools import groupby

def squeezer(s, txt):
    return ''.join(ch for ch, _ in groupby(txt, lambda x: x != s))

strings = ["hello", "world", "python"]
squeezers = ["l", "o", "t"]

for string, squeezer in zip(strings, squeezers):
    print(f"Original string: {string}")
    print(f"Modified string: {squeezer(string, squeezer)}")
```