```python
from kanren import run, eq, membero, var, conde

# Define the predefined lists of words
list1 = ('quick', 'lazy', 'brown', 'pink')
list2 = ('fox', 'dog', 'cat')

# Define the amb operator
def amb(*choices):
    return conde((eq(choices, choices),))

# Define the joins predicate
def joins(x, y):
    return eq(x[-1], y[0])

# Define the amb_example predicate
def amb_example():
    x, y, z = var(), var(), var()
    return run(0, (x, y, z), 
               (membero, x, list1),
               (membero, y, list2),
               (membero, z, list1),
               (joins, x, y),
               (joins, y, z))
```