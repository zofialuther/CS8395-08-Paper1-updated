```python
def pi_digits_generator():
    a = 1
    b = 1 / 2**0.5
    t = 1 / 4
    p = 1
    while True:
        a_new = (a + b) / 2
        b = (a * b)**0.5
        t -= p * (a - a_new)**2
        a = a_new
        p *= 2
        yield int((a + b)**2 / (4 * t))
```