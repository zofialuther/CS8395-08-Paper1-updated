```python
from itertools import combinations

def knapsack(items, limit):
    combos = []
    for i in range(1, len(items)+1):
        combos.extend(combinations(items, i))
    
    valid_combos = []
    for combo in combos:
        total_weight = sum(item[1] for item in combo)
        if total_weight <= limit:
            valid_combos.append(combo)
    
    max_value = 0
    best_combo = []
    for combo in valid_combos:
        total_value = sum(item[2] for item in combo)
        if total_value > max_value:
            max_value = total_value
            best_combo = combo
    
    print("Total value:", max_value)
    print("Items in best combination:", best_combo)

# Example usage
items = [('item1', 2, 10), ('item2', 3, 15), ('item3', 5, 30), ('item4', 7, 40)]
limit = 10
knapsack(items, limit)
```