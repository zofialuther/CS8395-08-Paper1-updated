```python
import pychr

@pychr.constraints
def loop(N):
    print(N)
    N += 1
    loop(N)
```