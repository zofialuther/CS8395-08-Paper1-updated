```python
import itertools

def pythagorean_triples():
    return ((a, b, c) for c in itertools.count(1) for a in range(1, c) for b in range(a, c) if a*a + b*b == c*c)

def pythagorean_triples_list_comprehension():
    return [(a, b, c) for c in range(1, 100) for a in range(1, c) for b in range(a, c) if a*a + b*b == c*c]

def pythagorean_triples_itertools():
    return list(itertools.islice(pythagorean_triples(), 10))

def main():
    print("Pythagorean triples using generator expression:")
    for triple in itertools.islice(pythagorean_triples(), 10):
        print(triple)
    
    print("\nPythagorean triples using list comprehension:")
    for triple in pythagorean_triples_list_comprehension():
        print(triple)
    
    print("\nPythagorean triples using itertools:")
    for triple in pythagorean_triples_itertools():
        print(triple)

if __name__ == "__main__":
    main()
```