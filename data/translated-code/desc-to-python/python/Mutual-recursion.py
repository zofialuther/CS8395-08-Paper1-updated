```python
def F(n):
    if n == 0:
        return 0
    else:
        return n - M(F(n-1))

def M(n):
    if n == 0:
        return 1
    else:
        return n - F(M(n-1))

for i in range(20):
    print("F({}) = {}".format(i, F(i)))
    print("M({}) = {}".format(i, M(i)))
```