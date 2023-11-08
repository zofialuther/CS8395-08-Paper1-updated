```python
import inspect

def myself(*args, **kwargs):
    frame = inspect.currentframe().f_back
    code = frame.f_code
    global_vars = frame.f_globals
    new_func = type(frame.f_locals['myself'])(*args, **kwargs)
    return new_func

factorial = myself(lambda x: 1 if x == 0 else x * myself(x-1))
print(factorial(5))
```