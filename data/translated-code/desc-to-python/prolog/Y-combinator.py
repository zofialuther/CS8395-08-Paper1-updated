def Y_combinator(f):
    def g(h):
        return lambda x: f(h(h))(x)
    return g(g)

def fibonacci_function(g):
    def inner_fibonacci_function(n):
        if n < 2:
            return n
        else:
            return g(n-1) + g(n-2)
    return inner_fibonacci_function

def factorial_function(g):
    def inner_factorial_function(n):
        if n <= 1:
            return 1
        else:
            return n * g(n-1)
    return inner_factorial_function

Y = Y_combinator
fibonacci = Y(fibonacci_function)
factorial = Y(factorial_function)

print(fibonacci(10))
print(factorial(10))