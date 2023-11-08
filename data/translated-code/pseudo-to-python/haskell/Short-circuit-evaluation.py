```python
import functools
import operator

def and_func(a, b):
    if not a:
        return False
    elif a and not b:
        return False
    else:
        return True

def or_func(a, b):
    if a:
        return True
    elif not a and b:
        return True
    else:
        return False

def a(p):
    return f"<a {p}>"

def b(p):
    return f"<b {p}>"

for p in [False, True]:
    for q in [False, True]:
        print(or_func(a(p), b(q)))
        print(and_func(a(p), b(q)))
```