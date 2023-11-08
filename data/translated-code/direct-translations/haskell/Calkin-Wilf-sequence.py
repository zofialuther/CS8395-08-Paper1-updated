```python
from typing import List, Tuple
from fractions import Fraction
from itertools import islice
from math import floor

# The infinite Calkin-Wilf sequence, a(n), starting with a(1) = 1.
def calkinWilfs() -> List[Fraction]:
    def next_term(x: Fraction) -> Fraction:
        return 1 / (x - floor(x))

    sequence = [Fraction(1, 1)]
    while True:
        sequence.append(next_term(sequence[-1]))
        yield sequence[-1]

# The index into the Calkin-Wilf sequence of a given rational number, starting
# with 1 at index 1.
def calkinWilfIdx(r: Fraction) -> int:
    def cf(r: Fraction) -> List[int]:
        result = []
        while r.denominator != 1:
            n = floor(r)
            result.append(n)
            r = 1 / (r - n)
        result.append(r.numerator)
        return result

    def rld(cf: List[int]) -> int:
        result = 0
        for i in range(len(cf) - 1, -1, -1):
            if i == len(cf) - 1:
                result = cf[i]
            else:
                result = cf[i] + 2 * result if i % 2 == 0 else result
        return result

    return rld(cf(r))

if __name__ == "__main__":
    cw_sequence = calkinWilfs()
    for i, r in enumerate(islice(cw_sequence, 20), 1):
        print(f"{i:2}  {r}")

    r = Fraction(83116, 51639)
    print(f"\n{r} is at index {calkinWilfIdx(r)} of the Calkin-Wilf sequence.")
```