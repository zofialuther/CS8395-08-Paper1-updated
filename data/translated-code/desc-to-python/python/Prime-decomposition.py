```python
import time

def fac(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
       factors.append(n)
    return factors

start_time = time.time()
result = fac(2**59 - 1)
end_time = time.time()

print("Prime factors:", result)
print("Time taken:", end_time - start_time, "seconds")
```