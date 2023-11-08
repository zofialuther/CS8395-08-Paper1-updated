from dataclasses import dataclass
import operator
from itertools import combinations

def lcs(xs, ys):
    return max((set(x) & set(y) for x in combinations(xs, len(ys)) for y in combinations(ys, len(xs))), key=len)

print(lcs("thisisatest", "testing123testing"))