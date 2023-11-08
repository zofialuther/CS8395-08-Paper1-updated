from typing import List, Tuple

Rings = List[Tuple[int, int, int, int, int, int, int]]

def rings(u: bool, digits: List[int]) -> Rings:
    return queen(u, digits)

def queen(u: bool, digits: List[int]) -> Rings:
    sorted_digits = sorted(digits, reverse=True)
    return [left_bishop(u, q, h, digits) for q in sorted_digits]

def left_bishop(u: bool, q: int, h: int, digits: List[int]) -> Rings:
    lRook = q + h
    ts = [d for d in digits if d <= h]
    if u:
        xs = [d for d in ts if d != q]
    else:
        xs = digits
    if lRook <= h:
        return [right_bishop(u, q, h, lb, digits, lRook) for lb in xs]
    else:
        return []

def right_bishop(u: bool, q: int, h: int, lb: int, digits: List[int], lRook: int) -> Rings:
    rRook = q + lb
    if (rRook <= h) and (not u or (rRook != lb)):
        ks = [d for d in digits if d not in [q, lb, lRook, rRook, rRook]]
        return [knights(u, lRook - rRook, lRook, lb, q, rRook, rRook, ks, k) for k in ks]
    else:
        return []

def knights(u: bool, rookDelta: int, lRook: int, lb: int, q: int, rb: int, rRook: int, ks: List[int], k: int) -> Rings:
    k2 = k + rookDelta
    valid_k2 = [k2 for k2 in ks if (not u) or (k2 not in [lRook, k, lb, q, rb, rRook])]
    return [(lRook, k, lb, q, rb, k2, rRook) for k2 in valid_k2]

def main() -> None:
    def f(k: str, xs: Rings) -> None:
        print(k)
        nl()
        for x in xs:
            print(x)
        nl()

    def nl() -> None:
        print()

    test_results = [
        ("rings True [1 .. 7]", rings(True, list(range(1, 8)))),
        ("rings True [3 .. 9]", rings(True, list(range(3, 10))),
        ("length (rings False [0 .. 9])", [len(rings(False, list(range(0, 10))))])
    ]

    for result in test_results:
        f(*result)

main()