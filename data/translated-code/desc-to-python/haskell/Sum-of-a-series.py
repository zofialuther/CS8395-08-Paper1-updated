```python
def seriesSum(f, lst):
    return foldr(lambda x, y: f(x) + y, 0, lst)

def inverseSquare(x):
    return 1 / (x ** 2)

def main():
    result = seriesSum(inverseSquare, range(1, 1001))
    print(result)

main()
```