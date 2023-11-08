```python
def member1(X, L):
    if L == []:
        return False
    if L[0] == X:
        return True
    return member1(X, L[1:])

def distinct(L):
    if L == []:
        return []
    if member1(L[0], L[1:]):
        return distinct(L[1:])
    else:
        return [L[0]] + distinct(L[1:])
```