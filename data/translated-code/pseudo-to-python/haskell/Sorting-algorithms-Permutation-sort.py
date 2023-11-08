```python
def permutationSort(l):
    p = []
    for permutation in permute(l):
        if sorted(permutation):
            p.append(permutation)
    return p[0]

def sorted(e1, e2, r):
    if e1 <= e2 and sorted(e2, r):
        return True
    else:
        return False

def permute(l):
    result = []
    for permutation in foldM(flip insert, l):
        result.append(permutation)
    return result

def insert(e, l):
    if not l:
        return [e]
    else:
        return [e] + insert(e, l[1:])
```