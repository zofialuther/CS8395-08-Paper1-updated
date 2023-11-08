```python
import threading

def takeMVar(mvar):
    return mvar.get()

def putMVar(mvar, value):
    mvar.put(value)

def tryTakeMVar(mvar):
    if not mvar.empty():
        return mvar.get()
    else:
        return None

def tryPutMVar(mvar, value):
    if not mvar.full():
        mvar.put(value)
        return True
    else:
        return False
```