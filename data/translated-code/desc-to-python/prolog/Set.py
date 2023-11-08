```python
# Predicates for set operations using ordered sets

# Create a set
def create_set(elements):
    return set(elements)

# Membership testing
def is_member(element, set):
    return element in set

# Union of two sets
def union(set1, set2):
    return set1.union(set2)

# Intersection of two sets
def intersection(set1, set2):
    return set1.intersection(set2)

# Difference between two sets
def difference(set1, set2):
    return set1.difference(set2)

# Subset comparison
def is_subset(subset, set):
    return subset.issubset(set)

# Equality comparison
def is_equal(set1, set2):
    return set1 == set2

# Proper subset comparison
def is_proper_subset(subset, set):
    return subset.issubset(set) and subset != set

# Add an element to a set
def add_element(element, set):
    set.add(element)
    return set

# Remove an element from a set
def remove_element(element, set):
    set.remove(element)
    return set
```