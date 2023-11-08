```python
# Python equivalent code

# Option 1: union of differences
def symmetric_difference(setA, setB):
    not_in_setA = setB.difference(setA)
    not_in_setB = setA.difference(setB)
    symmetric_difference = not_in_setA.union(not_in_setB)
    return symmetric_difference

# Option 2: union minus intersection
def symmetric_difference_2(setA, setB):
    union = setA.union(setB)
    intersection = setA.intersection(setB)
    symmetric_difference_2 = union.difference(intersection)
    return symmetric_difference_2

# Main code
setA = {"John", "Serena", "Bob", "Mary", "Serena"}
setB = {"Jim", "Mary", "John", "Jim", "Bob"}

# Present our initial data set
print("In set A:", setA)
print("In set B:", setB)

# Calculate symmetric differences using both options
sym_diff = symmetric_difference(setA, setB)
sym_diff_2 = symmetric_difference_2(setA, setB)

# Present the results
print("Symmetric Difference:", sym_diff)
print("Symmetric Difference 2:", sym_diff_2)
```