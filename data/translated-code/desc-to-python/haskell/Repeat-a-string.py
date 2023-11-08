```python
def repString(n, s):
    result = ""
    while n > 0:
        if n % 2 == 1:
            result += s
        s += s
        n = n // 2
    return result

def main():
    print(repString(500, "ha"))

main()
```