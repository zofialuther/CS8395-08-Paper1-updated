```python
def member1(X, lst):
    if not lst:
        return False
    if X == lst[0]:
        return True
    return member1(X, lst[1:])

def distinct(lst, C):
    if not lst:
        return
    if member1(lst[0], lst[1:]):
        distinct(lst[1:], C)
    else:
        C.append(lst[0])
        distinct(lst[1:], C)
```