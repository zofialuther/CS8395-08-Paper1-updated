```python
def normalize(ranges):
    ranges.sort(key=lambda x: x[0])
    return ranges

def consolidate(ranges):
    consolidated = [ranges[0]]
    for current in ranges[1:]:
        previous = consolidated[-1]
        if current[0] <= previous[1]:
            consolidated[-1] = [previous[0], max(previous[1], current[1])]
        else:
            consolidated.append(current)
    return consolidated

# Test block
test_ranges = [[1, 5], [3, 7], [8, 10], [9, 12], [15, 20]]
print("Original ranges:", test_ranges)
print("Consolidated ranges:", consolidate(normalize(test_ranges)))
```