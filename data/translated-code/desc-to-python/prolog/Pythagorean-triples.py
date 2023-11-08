```python
def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2

def count_triples(max_value):
    count = 0
    for a in range(1, max_value+1):
        for b in range(a, max_value+1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= max_value:
                count += 1
    return count

def generate_triples(max_value):
    triples = []
    for a in range(1, max_value+1):
        for b in range(a, max_value+1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= max_value:
                triples.append((a, b, int(c)))
    return triples

def show(max_value):
    primitive_count = count_triples(max_value)
    total_count = len(generate_triples(max_value))
    print(f"Up to {max_value}, there are {primitive_count} primitive triples and {total_count} total triples.")
```