```python
def getSierpinskiTriangle(n):
    if n == 0:
        return "  /\\  \n /  /\\ \n/__/__\\"
    else:
        smaller = getSierpinskiTriangle(n-1).split("\n")
        result = ""
        for line in smaller:
            result += " " * (2 ** (n-1)) + line + " " * (2 ** (n-1)) + "\n"
        return result

print(getSierpinskiTriangle(5))
```