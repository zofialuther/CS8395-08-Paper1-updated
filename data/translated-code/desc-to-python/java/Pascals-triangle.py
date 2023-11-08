```python
import math

class Pas:
    def pas(self, n):
        for i in range(n):
            for j in range(n-i+1):
                print(" ", end="")
            for j in range(i+1):
                print(self.ncr(i, j), " ", end="")
            print()

    def ncr(self, n, r):
        return int(self.fact(n) / (self.fact(r) * self.fact(n - r)))

    def fact(self, n):
        return math.factorial(n)

def main():
    p = Pas()
    p.pas(5)

if __name__ == "__main__":
    main()
```