```python
from fractions import Fraction

# A wrapper type for Fractions to make them look nicer when we print them.
class Rat:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __str__(self):
        return f"{self.n}/{self.d}"

# Convert a list of base b digits to its corresponding number.
# We assume the digits are valid base b numbers and that
# their order is from least to most significant.
def digitsToNum(b, digits):
    acc = digits[0]
    for i in range(1, len(digits)):
        acc = b * acc + digits[i]
    return acc

# Convert a number to the list of its base b digits.
# The order will be from least to most significant.
def numToDigits(b, n):
    if n == 0:
        return [0]
    else:
        result = []
        while n != 0:
            r = n % b
            result.append(r)
            n = n // b
        return result

# Return the n'th element in the base b van der Corput sequence.
# The base must be ≥ 2.
def vdc(b, n):
    if b < 2:
        raise ValueError("vdc: base must be ≥ 2")
    else:
        ds = list(reversed(numToDigits(b, n)))
        return Rat(digitsToNum(b, ds), b ** len(ds))

# Each base followed by a specified range of van der Corput numbers.
def printVdcRanges(bases, nums):
    for b in bases:
        rs = []
        for n in nums:
            rs.append(vdc(b, n))
        print(f"Base {b}: {rs}")

def main():
    printVdcRanges([2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    printVdcRanges([123], [50, 100, 150, 200, 250, 300])

main()
```