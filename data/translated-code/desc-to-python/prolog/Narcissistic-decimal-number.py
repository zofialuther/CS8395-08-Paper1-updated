```python
def digits(n):
    return [int(i) for i in str(n)]

def combi(lst, r):
    from itertools import combinations
    return list(combinations(lst, r))

def powSum(lst, r):
    return sum([i**r for i in lst])

def armstrong(exponent):
    armstrong_numbers = []
    for n in range(10**(exponent-1), 10**exponent):
        d = digits(n)
        if n == powSum(d, exponent):
            armstrong_numbers.append(n)
    return armstrong_numbers

def do():
    for exp in range(1, 8):
        print(f"Armstrong numbers for exponent {exp}: {armstrong(exp)}")

do()
```