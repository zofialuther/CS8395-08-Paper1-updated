```python
def fix(f):
    return (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))

factorial = fix(lambda f: lambda n: 1 if n == 0 else n * f(n-1))
fibonacci = fix(lambda f: lambda n: n if n <= 1 else f(n-1) + f(n-2))

Y = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
fibonacci_lazy = Y(lambda f: lambda n: n if n <= 1 else f(n-1) + f(n-2))

def main():
    for i in range(10):
        print(f"{i}! = {factorial(i)}")
    
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
        
    for i in range(10):
        print(f"Fibonacci_lazy({i}) = {fibonacci_lazy(i)}")

main()
```