```python
import functools

def fs(f, s):
    return [f(x) for x in s]

def f1(x):
    return x * 2

def f2(x):
    return x ** 2

fsf1 = functools.partial(fs, f1)
fsf2 = functools.partial(fs, f2)

# Testing the functionality
s = [1, 2, 3, 4, 5]
print(fs(f1, s))  # Expected output: [2, 4, 6, 8, 10]
print(fs(f2, s))  # Expected output: [1, 4, 9, 16, 25]
print(fsf1(s))  # Expected output: [2, 4, 6, 8, 10]
print(fsf2(s))  # Expected output: [1, 4, 9, 16, 25]
```