```python
from ctypes import CDLL

lib = CDLL("JNIDemo")

def callStrdup(s):
    return lib.callStrdup(s)

print(callStrdup("Hello World!"))
```