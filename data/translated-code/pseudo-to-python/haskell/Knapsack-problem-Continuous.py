```python
from operator import itemgetter
from functools import cmp_to_key
from textwrap import dedent

items = [ ("beef", (36, 3.8))
        , ("pork", (43, 5.4))
        , ("ham", (90, 3.6))
        , ("greaves", (45, 2.4))
        , ("flitch", (30, 4.0))
        , ("brawn", (56, 2.5))
        , ("welt", (67, 3.7))
        , ("salami", (95, 3.0))
        , ("sausage", (98, 5.9))
        ]

def unitWeight(item):
    name, (val, weight) = item
    return val / weight

def solution(k, items):
    items.sort(key=cmp_to_key(lambda x, y: 1 if unitWeight(x) < unitWeight(y) else -1))
    total_weight = 0
    for name, (val, weight) in items:
        if total_weight + weight < k:
            print(f"Take all the {name}")
            total_weight += weight
        else:
            remaining_weight = k - total_weight
            print(f"Take {remaining_weight:.2f} kg of the {name}")
            break

solution(15, items)
```