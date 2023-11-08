```python
import Control.Exception

def check(x, y):
    try:
        result = x / y
        return False
    except:
        return True
```