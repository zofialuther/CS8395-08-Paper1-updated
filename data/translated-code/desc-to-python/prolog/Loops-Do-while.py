```python
def do(value):
    if value % 6 == 0:
        return False
    print(value)
    return do(value + 1)

def wloop():
    do(0)

wloop()
```