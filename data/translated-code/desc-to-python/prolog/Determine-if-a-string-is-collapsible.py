```python
def collapse_(lst):
    if len(lst) < 2:
        return lst
    elif lst[0] == lst[1]:
        return collapse_(lst[1:])
    else:
        return [lst[0]] + collapse_(lst[1:])

def collapse(s):
    lst = list(s)
    collapsed_lst = collapse_(lst)
    return ''.join(collapsed_lst)
```