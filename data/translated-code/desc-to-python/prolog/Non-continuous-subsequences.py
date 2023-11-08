```python
def ncsubs(lst):
    result = set()
    for i in range(len(lst)):
        result = result.union(one_ncsubs(lst, i))
    return list(result)

def one_ncsubs(lst, index):
    if len(lst) == 0:
        return set()
    elif index == 0 or index == len(lst) - 1:
        return {tuple(lst)}
    else:
        return one_ncsubs(lst[:index] + lst[index + 1:], index - 1).union(one_ncsubs(lst[:index] + lst[index + 1:], index))

def extract_elem(lst, index):
    return lst[index]

def sublist(lst, index):
    return lst[index]
```