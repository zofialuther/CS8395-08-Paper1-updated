```python
def YCombinator(f):
    return (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

def main():
    y_comb = YCombinator(lambda f: lambda n: 1 if n == 0 else n * f(n-1))
    print(y_comb(10))

    y_comb = YCombinator(lambda f: lambda n: n if n <= 1 else f(n-1) + f(n-2))
    print(y_comb(10))

if __name__ == "__main__":
    main()
```