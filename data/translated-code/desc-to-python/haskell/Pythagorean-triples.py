```python
import math

def pytr(n):
    triples = [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a**2 + b**2 == c**2 and a + b + c <= n]
    return triples

def main():
    n = 100
    triples = pytr(n)
    primitive_triples = [(a, b, c) for (a, b, c) in triples if math.gcd(a, math.gcd(b, c)) == 1]
    print(f"Total number of triples: {len(triples)}")
    print(f"Number of primitive triples: {len(primitive_triples)}")

if __name__ == "__main__":
    main()
```