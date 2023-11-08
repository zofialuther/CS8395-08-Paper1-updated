```python
from ctypes import c_char_p, CDLL

# load the C library
libc = CDLL("libc.so.6")

# define the function signature for strdup
strdup = libc.strdup
strdup.restype = c_char_p
strdup.argtypes = [c_char_p]

# define the testC function
def testC():
    s = b"Hello World!"  # marshall the Haskell string "Hello World!" into a C string
    s2 = strdup(s)
    s2_hs = s2.decode('utf-8')  # marshall the C string called s2 into a Haskell string named s2_hs
    print(s2_hs)
    libc.free(s2)  # s is automatically freed by the strdup function once done

# call the testC function
testC()
```