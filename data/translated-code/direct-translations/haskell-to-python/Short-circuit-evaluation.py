```python
from functools import reduce

def a(p):
    return f"<a {p}>"

def b(p):
    return f"<b {p}>"

def my_and(x, y):
    if not x:
        return False
    else:
        return y

def my_or(x, y):
    if x:
        return True
    else:
        return y

def main():
    values = [my_or(a(p), b(q)) for p in [False, True] for q in [False, True]] + [my_and(a(p), b(q)) for p in [False, True] for q in [False, True]]
    for value in values:
        print(value)

if __name__ == "__main__":
    main()
```