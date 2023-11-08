```python
def compose(f, g):
    return lambda x: f(g(x))

def repeat(f, n):
    return lambda x: x if n == 0 else repeat(f, n-1)(f(x))

def test():
    add1 = lambda x: x + 1
    mult2 = lambda x: x * 2
    assert repeat(add1, 3)(5) == 8
    assert repeat(compose(add1, mult2), 2)(3) == 9
    print("All test cases pass")

if __name__ == "__main__":
    test()
```