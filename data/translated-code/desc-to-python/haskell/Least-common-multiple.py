```python
def lcm(x, y):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    if x == 0 or y == 0:
        return 0
    else:
        return abs((x // gcd(x, y)) * y)
```