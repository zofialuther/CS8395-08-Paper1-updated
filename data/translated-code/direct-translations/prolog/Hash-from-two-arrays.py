```python
hash_table = {}

def make_hash(keys, values):
    for key, value in zip(keys, values):
        hash_table[key] = value

make_hash(['un', 'deux', 'trois'], [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])

def make_hash_pure(keys, values):
    return [ (key, value) for key, value in zip(keys, values) ]

hash_table_pure = make_hash_pure(['un', 'deux', 'trois'], [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
```