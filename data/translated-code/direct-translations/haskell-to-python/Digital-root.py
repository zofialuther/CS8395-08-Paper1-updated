from typing import Tuple

def digSum(base: int, n: int) -> int:
    def f(n: int) -> Tuple[int, int]:
        if n == 0:
            return None
        else:
            return (n // base, n % base)
    return sum(unfoldr(f, n))

def digRoot(base: int, n: int) -> Tuple[int, int]:
    def iterateFunc(pair: Tuple[int, int]) -> Tuple[int, int]:
        return (pair[0] + 1, digSum(base, pair[1]))
    return next(((i, result) for i, result in enumerate(iterate(iterateFunc, (0, n))) if result < base), None)

def main() -> None:
    print("in base 10:")
    for number in [627615, 39390, 588225, 393900588225]:
        print((number, digRoot(10, number)))

if __name__ == "__main__":
    main()