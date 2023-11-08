```python
from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'weight', 'value', 'number'])

def anyvalidcomb(items, max_weight):
    bagged_items = []
    for i in range(1, len(items)+1):
        for combo in combinations(items, i):
            total_weight = sum(item.weight for item in combo)
            if total_weight <= max_weight:
                bagged_items = combo
    bagged_value = sum(item.value for item in bagged_items)
    bagged_weight = sum(item.weight for item in bagged_items)
    print("Bagged items:", bagged_items)
    print("Total value:", bagged_value)
    print("Total weight:", bagged_weight)

# Usage
items = [Item('item1', 10, 100, 2), Item('item2', 20, 150, 1), Item('item3', 15, 120, 3)]
max_weight = 30
anyvalidcomb(items, max_weight)
```