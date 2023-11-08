from typing import List
from functools import reduce
from operator import add

def ffr(n: int) -> int:
    rl = [1] + fig(1, list(range(2, n+1)))
    return rl[n-1]

def fig(n: int, xs: List[int]) -> List[int]:
    if xs:
        n_ = n + xs[0]
        return [n_] + fig(n_, [x for x in xs if x != n_])
    else:
        return []

def ffs(n: int) -> int:
    rl = [2] + figDiff(1, list(range(2, n+1)))
    return rl[n]

def figDiff(n: int, xs: List[int]) -> List[int]:
    if xs:
        n_ = n + xs[0]
        return [xs[0]] + figDiff(n_, [x for x in xs if x != n_])
    else:
        return []

def main():
    print(list(map(ffr, range(1, 11)))
    i1000 = sorted(list(map(ffr, range(1, 41))) + list(map(ffs, range(1, 961)))
    print(i1000 == list(range(1, 1001)))

if __name__ == "__main__":
    main()