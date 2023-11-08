```python
# Python does not have a built-in function for bogosort, so here is a simple implementation

import random

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

def bogosort(lst):
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst

# Example usage:
my_list = [3, 2, 5, 1, 4]
sorted_list = bogosort(my_list)
print(sorted_list)
```