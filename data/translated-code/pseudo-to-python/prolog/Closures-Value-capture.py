```python
def make_func(I):
    return lambda X: X**2

def closure():
    Lnum = list(range(1, 11))
    Lfunc = []
    for num in Lnum:
        Lfunc.append(make_func(num))
    for num, func in zip(Lnum, Lfunc):
        print(func(num))

closure()
```