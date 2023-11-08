```python
def all_equal(a, b, c, d, e, f, g):
    return (a + b) == (c + d) == (e + f) == (g)

def foursquares(range_of_numbers, print_solutions=False):
    solutions = []
    for a in range(range_of_numbers):
        for b in range(range_of_numbers):
            for c in range(range_of_numbers):
                for d in range(range_of_numbers):
                    for e in range(range_of_numbers):
                        for f in range(range_of_numbers):
                            for g in range(range_of_numbers):
                                if len(set([a, b, c, d, e, f, g])) == 7:
                                    if all_equal(a, b, c, d, e, f, g):
                                        if print_solutions:
                                            print(a, b, c, d, e, f, g)
                                        solutions.append((a, b, c, d, e, f, g))
    print(len(solutions), "solutions found within the range")
```