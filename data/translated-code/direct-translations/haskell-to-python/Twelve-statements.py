```python
from typing import List, Tuple
from dataclasses import dataclass

def tf(predicates: List[List[int] -> bool]) -> List[List[int]]:
    return [traverse(lambda _: [1, 0], predicates)]

def wrongness(ns: List[int], ps: List[List[int] -> bool]) -> List[int]:
    return findIndices(lambda x: x, zipWith(lambda x, y: x != y, ns, map(lambda p: fromEnum(p(ns)), ps)))

@dataclass
class Statement:
    func: int
    condition: List[int]
    result: bool

def statements() -> List[List[int] -> bool]:
    def contains(s: int, x: List[int], b: List[int]) -> bool:
        return s == (sum(map(lambda i: b[i], filter(lambda i: i < len(b), x))))

    def implies(a: int, x: List[int], b: List[int]) -> bool:
        return b[a] == 0 or all(map(lambda i: b[i] == 1, x))

    return [
        lambda ns: len(ns) == 12,
        lambda ns: contains(3, list(range(len(statements()) - 6, len(statements()))), ns),
        lambda ns: contains(2, list(range(1, len(statements()), 2)), ns),
        lambda ns: implies(4, list(range(4, 7)), ns),
        lambda ns: contains(0, list(range(1, 4)), ns),
        lambda ns: contains(4, list(range(0, len(ns), 2)), ns),
        lambda ns: contains(1, [1, 2], ns),
        lambda ns: implies(6, list(range(4, 7)), ns),
        lambda ns: contains(3, list(range(0, 6)), ns),
        lambda ns: contains(2, [10, 11], ns),
        lambda ns: contains(1, [6, 7, 8], ns),
        lambda ns: contains(4, list(range(0, 11)), ns)
    ]

def testall(s: List[List[int] -> bool], n: int) -> List[Tuple[List[int], List[int]]]:
    return [(b, [wrongness(b, s)]) for b in tf(s) if len(wrongness(b, s)) == n]

def main() -> None:
    t = testall(statements(), 0)
    print("Answer")
    for result in t:
        print(result)
    print("Near misses")
    t = testall(statements(), 1)
    for result in t:
        print(result)
```