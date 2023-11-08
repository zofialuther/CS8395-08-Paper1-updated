```python
import os
from os import path
from shutil import move
import tempfile

def hInteract(f, input_handle, output_handle):
    contents = input_handle.read()
    result = f(contents)
    output_handle.write(result)

def processByTemp(f, name):
    with open(name, 'r') as hIn:
        tmp = name + "$"
        with open(tmp, 'w') as hOut:
            f(hIn, hOut)
    os.remove(name)
    move(tmp, name)

def process(f, strings):
    if not strings:
        f(sys.stdin, sys.stdout)
    else:
        mapM_(processByTemp(f, strings))
```