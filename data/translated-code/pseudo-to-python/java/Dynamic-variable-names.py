```python
def main(args):
    vars = {}
    vars["Variable name"] = 3
    vars["Next variable name"] = 5
    str = input()
    vars[str] = int(input())
    print(vars["Variable name"])
    print(vars[str])
```