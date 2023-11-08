```python
def floyd(n):
    triangle = []
    for i in range(1, n+1):
        triangle.append(nextFloyd(triangle[-1] if triangle else [], i))
    return triangle

def nextFloyd(prevRow, rowNumber):
    return [sum(range(1, i+1)) for i in range(1, rowNumber+1)] 

def showFloyd(triangle):
    return '\n'.join(' '.join(str(num) for num in row) for row in triangle)

def main():
    triangle = floyd(5)
    print(showFloyd(triangle))

main()
```