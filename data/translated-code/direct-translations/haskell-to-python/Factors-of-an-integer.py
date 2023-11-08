```python
def factorsO(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

print(factorsO(120))
print(factorsO(12041111117))
```