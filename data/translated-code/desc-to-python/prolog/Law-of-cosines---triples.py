```python
def is_solution(a, b, c, limit):
    return a**2 + b**2 == c**2 and c <= limit

def find_solutions(limit):
    solutions = []
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a**2 + b**2)**0.5
            if is_solution(a, b, c, limit):
                solutions.append((a, b, int(c)))
    return solutions

def write_triples(angle, limit):
    solutions = find_solutions(limit)
    print(f"Number of solutions for angle {angle}: {len(solutions)}")
    print(f"Pythagorean triples for angle {angle}: {solutions}")

def main():
    write_triples(60, 100)
    write_triples(90, 100)
    write_triples(120, 100)

if __name__ == "__main__":
    main()
```