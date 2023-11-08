```python
from functools import reduce

def loop(func, initial_state, list_of_lists):
    return reduce(func, [reduce(func, inner_list, initial_state) for inner_list in list_of_lists], initial_state)

def example(a, b):
    return a + b, a * b

initial_state = (0, 1)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = loop(example, initial_state, list_of_lists)
print(result)
```