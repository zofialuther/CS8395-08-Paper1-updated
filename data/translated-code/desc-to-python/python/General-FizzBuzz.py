```python
from collections import defaultdict

def fizz_buzz(n, mods):
    results = defaultdict(str)
    for i in range(1, n+1):
        for divisor, string in mods:
            if i % divisor == 0:
                results[i] += string
        if not results[i]:
            results[i] = str(i)
    for val in results.values():
        print(val)

# Example usage:
# fizz_buzz(20, [(3, "Fizz"), (5, "Buzz")])
```