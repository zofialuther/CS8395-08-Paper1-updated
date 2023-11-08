```python
def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def add(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))

def multiply(m, n):
    return lambda f: m(n(f))

def to_integer(n):
    return n(lambda x: x + 1)(0)

def from_integer(n):
    if n == 0:
        return zero
    else:
        return successor(from_integer(n-1))

def main():
    num1 = from_integer(5)
    num2 = from_integer(3)

    print(to_integer(add(num1, num2)))
    print(to_integer(multiply(num1, num2)))

main()
```