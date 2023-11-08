```python
def fibonacci(n):
    if n < 0:
        return "Error: Input must be a non-negative integer"
    else:
        def fib_recursive(f):
            def g(x):
                if x == 0:
                    return 0
                elif x == 1:
                    return 1
                else:
                    return f(x-1) + f(x-2)
            return g
        y_combinator = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
        fib = y_combinator(fib_recursive)
        return fib(n)
```