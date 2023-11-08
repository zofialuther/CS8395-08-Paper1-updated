```python
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def main():
    for i in range(1, 10):
        print(isqrt(i))
    
    for i in range(1, 10):
        num = i * 49 + 7
        print(isqrt(num))

main()
```