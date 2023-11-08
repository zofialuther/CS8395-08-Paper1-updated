from typing import List

def repCycles(cs: str) -> List[str]:
    n = len(cs)
    return list(filter(lambda x: cs == (x * (n // len(x)))[:n], [cs[:i] for i in range(n // 2, 0, -1)]))

def main() -> None:
    test_cases = [
        "1001110011",
        "1110111011",
        "0010010010",
        "1010101010",
        "1111111111",
        "0100101101",
        "0100100",
        "101",
        "11",
        "00",
        "1"
    ]
    print(fTable("Longest cycles:\n", lambda x: x, lambda x: "n/a" if not x else x[-1], repCycles, test_cases)

def fTable(s: str, xShow, fxShow, f, xs: List) -> str:
    def rjust(n, c):
        return lambda x: (c * (n - len(x))) + x
    w = max(len(xShow(x)) for x in xs)
    return '\n'.join([s] + [rjust(w, ' ')(xShow(x)) + " -> " + fxShow(f(x)) for x in xs])