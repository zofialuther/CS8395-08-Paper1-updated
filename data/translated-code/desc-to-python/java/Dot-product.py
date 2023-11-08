```python
def dotProd(a, b):
    if len(a) != len(b):
        return "Arrays must have the same dimensions"
    
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    
    return result

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

print(dotProd(a, b))
```