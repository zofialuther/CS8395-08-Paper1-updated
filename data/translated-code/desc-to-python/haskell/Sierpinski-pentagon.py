```python
def transform_shape(shape, s):
    shape.scale(s)
    shape.rotate(36)
    for angle in range(0, 289, 36):
        shape.duplicate(angle)
```