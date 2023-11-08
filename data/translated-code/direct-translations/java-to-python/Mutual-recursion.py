```python
F_MAP = {}
M_MAP = {}

def f(n):
    if n in F_MAP:
        return F_MAP[n]
    fn = 1 if n == 0 else n - m(f(n - 1))
    F_MAP[n] = fn
    return fn

def m(n):
    if n in M_MAP:
        return M_MAP[n]
    mn = 0 if n == 0 else n - f(m(n - 1))
    M_MAP[n] = mn
    return mn

max_val = 20
print(f"First {max_val} values of the Female sequence:")
for i in range(max_val):
    print(f"  f({i}) = {f(i)}")

print(f"First {max_val} values of the Male sequence:")
for i in range(max_val):
    print(f"  m({i}) = {m(i)}")
```