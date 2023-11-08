```python
class Amb:
    def __init__(self):
        self.choices = []

    def amb(self, *options):
        self.choices.append(iter(options))

    def iterate(self):
        if self.choices:
            return next(self.choices[-1], None)
        return None

    def solve(self, *constraints):
        for _ in range(100):
            solution = [self.iterate() for _ in range(len(constraints))]
            if all(constraint(*solution) for constraint in constraints):
                return solution
        return None

# Example usage
def pythagorean_triples(a, b, c):
    return a**2 + b**2 == c**2

amb = Amb()
amb.amb(*range(1, 100))
result = amb.solve(pythagorean_triples)
print(result)
```