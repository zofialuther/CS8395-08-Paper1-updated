```python
from typing import List, Dict, Any

# Implementation 1: Using side effects
def create_hash_table_side_effects(keys: List[Any], values: List[Any]) -> Dict[Any, Any]:
    hash_table = {}
    for i in range(len(keys)):
        assert keys[i] not in hash_table, "Key already exists in hash table"
        hash_table[keys[i]] = values[i]
    return hash_table

# Implementation 2: Pure function
def create_hash_table_pure(keys: List[Any], values: List[Any]) -> Dict[Any, Any]:
    return {keys[i]: values[i] for i in range(len(keys))}

# Using the pure function to create the hash table
hash_table = create_hash_table_pure(['a', 'b', 'c'], [1, 2, 3])

# Asserting elements of the hash table using findall
assert hash_table['a'] == 1
assert hash_table['b'] == 2
assert hash_table['c'] == 3
```