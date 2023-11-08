```python
def foo(X):
    if not isinstance(X, int):
        raise Exception("X is not even an integer")
    if X < 1 or X > 10:
        raise Exception("X must be between 1 and 10")
    print("X is a valid number")

def handle(ex):
    if ex == "a":
        print("Caught exception type a")
    else:
        raise ex

def go(X):
    try:
        foo(X)
    except Exception as ex:
        handle(ex)
```