```python
from fractions import Fraction

def farey(n):
    seq = [Fraction(0, 1), Fraction(1, 1)]
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        seq.insert(c, Fraction(a + k * c, b + k * d))
    return seq

def fareys(n, func):
    seq = farey(n)
    for i in range(n, 1, -1):
        func(seq)
        seq.pop(i - 2)
    return seq

def fprint(seq):
    print(", ".join(showFracs(seq)))

def showFracs(seq):
    return [str(f) for f in seq]

def main():
    for i in range(2, 6):
        seq = farey(i)
        print(f"Farey sequence of order {i}:")
        fprint(seq)
        print(f"Length: {len(seq)}")

if __name__ == "__main__":
    main()
```