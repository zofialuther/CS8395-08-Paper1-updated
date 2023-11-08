```python
def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def add(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))

def multiply(m, n):
    return lambda f: m(n(f))

def exponentiate(m, n):
    return n(m)

def int_church(n):
    return n(lambda x: x + 1)(0)

def run():
    num1 = int_church(successor(successor(zero)))
    num2 = int_church(successor(zero))
    result_add = int_church(add(num1, num2))
    result_multiply = int_church(multiply(num1, num2))
    result_exponentiate = int_church(exponentiate(num1, num2))
    print(result_add, result_multiply, result_exponentiate)

run()
```