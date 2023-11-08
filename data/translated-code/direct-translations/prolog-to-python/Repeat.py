```python
def repeat(_, 0):
    pass

def repeat(Callable, Times):
    if Times > 0:
        Callable()
        repeat(Callable, Times - 1)

def test():
    print('Hello, World')

def test_with_name(Name):
    print(f'Hello, {Name}')
```