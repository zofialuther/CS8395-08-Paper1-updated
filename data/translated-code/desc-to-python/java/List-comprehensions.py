```python
# Python does not have interfaces like Java, but we can achieve similar functionality using classes and methods

class PythagoreanTriple:
    @staticmethod
    def run(limit):
        triples = [(a, b, c) for c in range(1, limit) for b in range(1, c) for a in range(1, b) if a**2 + b**2 == c**2]
        return triples

# Example usage
limit = 20
result = PythagoreanTriple.run(limit)
print(result)
```