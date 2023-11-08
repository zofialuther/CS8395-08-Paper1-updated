```python
# Python code for list comprehension with operators and predicates

# Define operators and predicates for list comprehension
def list_comprehension(var, start, end, condition=None):
    if condition:
        return [var for var in range(start, end) if condition(var)]
    else:
        return [var for var in range(start, end)]

# Example usage
result1 = list_comprehension(x, 1, 10)
result2 = list_comprehension(y, 1, 10, lambda y: y % 2 == 0)
```