```python
import lambda

def make_closure():
    funcs = []
    for i in range(1, 11):
        funcs.append(lambda x, i=i: x**i)
    return funcs

def call_func(funcs):
    for i, func in enumerate(funcs, start=1):
        print(f"Number: {i}, Result: {func(i)}")

funcs = make_closure()
call_func(funcs)
```