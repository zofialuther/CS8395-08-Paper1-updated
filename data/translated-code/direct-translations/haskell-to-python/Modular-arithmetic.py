from Data.Modular import *

def f(x: ℤ/13) -> ℤ/13:
    return x**100 + x + 1

def main() -> None:
    print(f(10))

if __name__ == "__main__":
    main()