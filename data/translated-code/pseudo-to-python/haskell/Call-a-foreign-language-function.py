```python
from ctypes import CDLL, c_char_p

libc = CDLL("libc.so.6")

def testC():
    s = b"Hello World!"
    strdup = libc.strdup
    strdup.restype = c_char_p
    s2 = strdup(s)
    s2_hs = s2.decode('utf-8')
    print(s2_hs)
    libc.free(s2)
```