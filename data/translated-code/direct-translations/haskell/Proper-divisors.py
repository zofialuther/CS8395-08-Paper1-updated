```python
from sympy import factorint

def properDivisors(n):
    factors = factorint(n)
    divisors = [1]
    for prime, exp in factors.items():
        divisors.extend([p * prime**i for i in range(1, exp+1) for p in divisors])
    return sorted(divisors)[:-1]

def fTable(s, xShow, fxShow, f, xs):
    def rjust(n, c, s):
        return s.rjust(n, c)
    
    w = max(len(xShow(x)) for x in xs)
    result = [s]
    for x in xs:
        result.append(rjust(w, ' ', xShow(x)) + " -> " + fxShow(f(x)))
    return '\n'.join(result)

def main():
    print(fTable("Proper divisors of [1..10]:", str, str, properDivisors, list(range(1, 11)))
    
    print("")
    print("A number in the range 1 to 20,000 with the most proper divisors,")
    print("as (number, count of proper divisors):")
    print("")
    numbers_with_divisors = [(i, len(properDivisors(i))) for i in range(1, 20001)]
    max_divisors = max(numbers_with_divisors, key=lambda x: x[1])
    print(max_divisors)

if __name__ == "__main__":
    main()
```