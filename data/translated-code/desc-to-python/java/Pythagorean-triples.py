```python
# Python code to calculate the number of Pythagorean triples with a given perimeter limit
# Using recursive function to generate triples and counting total number of triples and primitive triples

import math

def parChild(a, b, c, limit, triples, primTriples):
    perimeter = a + b + c
    if perimeter <= limit:
        triples[0] += 1
        if math.gcd(a, b, c) == 1:
            primTriples[0] += 1
        parChild(a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c, limit, triples, primTriples)
        parChild(a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c, limit, triples, primTriples)
        parChild(-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c, limit, triples, primTriples)

limit = 100
triples = [0]
primTriples = [0]
parChild(3, 4, 5, limit, triples, primTriples)
print("Total number of triples with perimeter less than or equal to", limit, "is", triples[0])
print("Number of primitive triples with perimeter less than or equal to", limit, "is", primTriples[0])
```