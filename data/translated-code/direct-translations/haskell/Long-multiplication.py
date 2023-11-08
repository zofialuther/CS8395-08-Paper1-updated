from typing import List
from itertools import zip_longest

def longmult(x: int, y: int) -> int:
    digits_x = digits(x)
    digits_y = digits(y)
    return sum(int(''.join(map(str, row))) * (10 ** i) for i, row in enumerate(polymul(digits_x, digits_y)))

def polymul(xs: List[int], ys: List[int]) -> List[int]:
    return [sum(a * b for a, b in row) for row in zip_longest([0] * len(ys), *([x * y for y in ys] for x in xs), fillvalue=0)]

def digits(n: int) -> List[int]:
    return [int(d) for d in str(n)]

print(longmult(2 ** 64, 2 ** 64))