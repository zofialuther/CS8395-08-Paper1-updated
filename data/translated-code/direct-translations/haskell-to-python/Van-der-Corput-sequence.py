```python
from fractions import Fraction
from typing import List, Tuple

# A wrapper type for Fractions to make them look nicer when we print them.
class Rat:
    def __init__(self, n: Fraction):
        self.n = n

    def __str__(self):
        return f"{self.n.numerator}/{self.n.denominator}"

# Convert a list of base b digits to its corresponding number.
def digits_to_num(b: int, digits: List[int]) -> int:
    return sum(d * b ** i for i, d in enumerate(digits[::-1]))

# Convert a number to the list of its base b digits.
def num_to_digits(b: int, n: int) -> List[int]:
    if n == 0:
        return [0]
    else:
        digits = []
        while n:
            n, r = divmod(n, b)
            digits.append(r)
        return digits

# Return the n'th element in the base b van der Corput sequence.
def vdc(b: int, n: int) -> Rat:
    if b < 2:
        raise ValueError("vdc: base must be ≥ 2")
    else:
        ds = num_to_digits(b, n)
        return Rat(Fraction(digits_to_num(b, ds), b ** len(ds)))

# Each base followed by a specified range of van der Corput numbers.
def print_vdc_ranges(data: Tuple[List[int], List[int]]) -> None:
    bases, nums = data
    for b in bases:
        rs = [vdc(b, num) for num in nums]
        print(f"Base {b}:", end="")
        for r in rs:
            print(f" {r}", end="")
        print()

if __name__ == "__main__":
    # Small bases:
    print_vdc_ranges(([2, 3, 4, 5], list(range(10))))
    print()

    # Base 123:
    print_vdc_ranges(([123], list(range(50, 301, 50)))
```