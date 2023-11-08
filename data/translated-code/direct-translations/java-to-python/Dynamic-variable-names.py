```python
def main(*args):
    vars = {}
    vars["Variable name"] = 3  # declaration of variables
    vars["Next variable name"] = 5
    str = input()
    vars[str] = int(input())  # accepting name and value from user

    print(vars["Variable name"])  # printing of values
    print(vars[str])
```