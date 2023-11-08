```python
def compose(F, G):
    return lambda x: F(G(x))
```