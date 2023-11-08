```python
class Logger:
    def write(self, s: str) -> None:
        pass

instance_IO = Logger()
instance_IO.write = lambda s: print(s, end='')

instance_Writer = Logger()
instance_Writer.write = lambda s: print(s, end='')

def verbose2(f, x, y):
    res = f(x, y)
    instance_Writer.write(f"{x}, {y} ==> {res}\n")
    return res
```