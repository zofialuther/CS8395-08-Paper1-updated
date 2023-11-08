```python
def transpose(matrix):
    if not matrix:
        return []
    else:
        return [list(row) for row in zip(*matrix)]
```