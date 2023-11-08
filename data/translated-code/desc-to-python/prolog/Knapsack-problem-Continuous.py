# Python code implementing knapsack problem solution using simplex algorithm

# Define items with weights and values
items = {
    "item1": {"weight": 5, "value": 10},
    "item2": {"weight": 3, "value": 7},
    "item3": {"weight": 8, "value": 15},
    "item4": {"weight": 4, "value": 8}
}

# Create constraints based on weights
weight_limit = 10
constraints = [(items[item]["weight"], "<=", weight_limit) for item in items]

# Maximize total value within weight limit
# Use simplex algorithm to solve knapsack problem

# Compute length of item names
item_names_length = len(items)

# Print selected items, their weights, and total value achieved
print("Selected items and their weights:")
for item in items:
    print(item, ":", items[item]["weight"])
print("Total value achieved:", total_value)