from typing import Callable

def repeat(n: int, fun: Callable[[int], None]) -> None:
    for i in range(n):
        fun(i + 1)

def main() -> None:
    repeat(3, lambda x: print("Example " + str(x)))

if __name__ == "__main__":
    main()