```python
def Y(f):
    return (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

def factorial_recursive(fact):
    def helper(n):
        if n == 0:
            return 1
        else:
            return n * fact(n-1)
    return helper

def fibonacci_recursive(fib):
    def helper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    return helper

factorial = Y(factorial_recursive)
fibonacci = Y(fibonacci_recursive)

factorial_sequence = [factorial(n) for n in range(10)]
fibonacci_sequence = [fibonacci(n) for n in range(10)]

print(factorial_sequence)
print(fibonacci_sequence)
```