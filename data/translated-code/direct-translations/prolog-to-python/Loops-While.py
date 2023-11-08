```python
def while_loop(X):
    if X == 0:
        return
    else:
        print(X)
        X1 = X // 2
        while_loop(X1)

while_loop(10)
```