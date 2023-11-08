```python
def ethMult(n, m):
    result = 0
    while n > 0:
        if n % 2 != 0:
            result += m
        n = n // 2
        m = m * 2
    return result

def half(num):
    return num // 2

def addedWhereOdd(a, x, d):
    if d % 2 != 0:
        return a + x
    else:
        return a

def main():
    print(ethMult(17, 34))
    print(ethMult(10, 15))
    print(ethMult(8, 11))

main()
```