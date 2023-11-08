```python
from itertools import islice

def is_prefix_of(a, b):
    return b.startswith(a)

def is_suffix_of(a, b):
    return b.endswith(a)

def is_infix_of(a, b):
    return a in b

def find_indices(a, b):
    indices = []
    for i in range(len(b)):
        if is_prefix_of(a, b[i:]):
            indices.append(i)
    return indices

print(is_prefix_of("abc", "abcdefg"))  # True
print(is_suffix_of("efg", "abcdefg"))  # True
print(is_infix_of("bcd", "abcdefg"))  # True
print(is_infix_of("abc", "abcdefg"))  # True
print(find_indices("ab", "abcdefabqqab"))  # [0, 6, 10]
```