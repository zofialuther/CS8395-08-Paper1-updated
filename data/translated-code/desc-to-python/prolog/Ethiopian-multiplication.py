```python
def mul(x, y):
    if x == 1:
        return y
    else:
        return mul(x-1, y*2)

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def add_if_odd(x, y, z):
    if x % 2 != 0:
        return y + z
    else:
        return y

def test():
    result = mul(17, 34)
    print(result)
```