```python
def getSierpinskiTriangle(n):
    if n == 0:
        return "*"
    
    s = getSierpinskiTriangle(n - 1)
    split = s.split("\n")
    length = len(split)
    sb = ""
    
    # Top triangle
    top = buildSpace(2**(n - 1))
    for i in range(length):
        sb += top + split[i] + "\n"
    
    # Two triangles side by side
    for i in range(length):
        sb += split[i] + buildSpace(length - i) + split[i] + "\n"
    
    return sb

def buildSpace(n):
    sb = ""
    while n > 0:
        sb += " "
        n -= 1
    return sb

print(getSierpinskiTriangle(4))
```