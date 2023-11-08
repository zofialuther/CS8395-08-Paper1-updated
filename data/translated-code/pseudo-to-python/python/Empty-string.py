```python
s = ''
# or:
s = str()

if not s or s == '':
   print("String is empty")

if len(s) == 0:
    print("String is empty")
else:
    print("String not empty")

def emptystring(s):
    if isinstance(s, str) or isinstance(s, unicode):
        if len(s) == 0:
            return True
        else:
            return False
    elif s is None:
        return True
```