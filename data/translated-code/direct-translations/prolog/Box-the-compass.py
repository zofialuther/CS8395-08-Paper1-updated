```python
def compassangle(index, name, heading, angle):
    if angle:
        resolve_index(angle, index)
    else:
        resolve_index(index)

def resolve_index(angle, index):
    n = angle / 11.25 + 0.5
    i = int(n)
    index = (i % 32) + 1
```