```python
def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def church_to_int(n):
    return n(lambda x: x + 1)(0)

def add(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))

def multiply(m, n):
    return lambda f: m(n(f))

def power(m, n):
    return n(m)

def test_arithmetic_operations():
    three = successor(successor(successor(zero)))
    four = successor(successor(successor(successor(zero)))
    
    print(church_to_int(add(three, four)))
    print(church_to_int(multiply(three, four)))
    print(church_to_int(power(three, four)))

test_arithmetic_operations()
```