```python
def main():
    result = queens(8)
    for r in result:
        print(r)

def queens(n):
    return foldM(f, [], list(range(1, n+1)))

def f(qs, _):
    return [q:qs for q in list(range(1, n+1)) if q not in qs and notDiag(q, qs)]

def notDiag(q, qs):
    return all(abs(q - qi) != i for qi, i in zip(qs, list(range(1, len(qs)+1))))
```