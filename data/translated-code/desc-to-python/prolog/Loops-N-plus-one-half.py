```python
def generate_values():
    for i in range(1, 10):
        if i != 9:
            print(i, end=", ")
        else:
            print(i)
            raise StopIteration

try:
    generate_values()
except StopIteration:
    pass
```