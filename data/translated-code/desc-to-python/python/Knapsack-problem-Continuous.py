items = [
    {"name": "item1", "weight": 10, "value": 60},
    {"name": "item2", "weight": 20, "value": 100},
    {"name": "item3", "weight": 30, "value": 120}
]

max_weight = 50
selected_items = []

items.sort(key=lambda x: x["value"]/x["weight"], reverse=True)

total_weight = 0
total_value = 0

for item in items:
    if total_weight + item["weight"] <= max_weight:
        selected_items.append(item)
        total_weight += item["weight"]
        total_value += item["value"]

print("Selected items:", selected_items)
print("Total weight:", total_weight)
print("Total value:", total_value)