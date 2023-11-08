```python
def fun(x, y):
    y = 2 * x

L = [1, 2, 3, 4, 5]
result = map(lambda x: fun(x, x), L)
```