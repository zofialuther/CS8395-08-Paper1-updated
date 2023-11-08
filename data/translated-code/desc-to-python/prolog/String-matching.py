```python
# Python code does not have direct equivalents for Prolog predicates and list manipulation, but a similar functionality can be achieved using Python lists and functions.

def starts_with(list1, list2):
    return list1[:len(list2)] == list2

def contains(list1, list2):
    return any(list2 == list1[i:i+len(list2)] for i in range(len(list1) - len(list2) + 1)

def contains_at_position(list1, list2, position):
    return list1[position:position+len(list2)] == list2

def ends_with(list1, list2):
    return list1[-len(list2):] == list2
```