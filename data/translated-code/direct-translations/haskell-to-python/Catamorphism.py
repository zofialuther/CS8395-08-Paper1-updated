from dataclasses import dataclass
from typing import List

@dataclass
class Sum:
    value: int

    def __add__(self, other):
        return Sum(self.value + other.value)

@dataclass
class Product:
    value: int

    def __mul__(self, other):
        return Product(self.value * other.value)

def main():
    xs = list(range(1, 11))
    print('\n'.join([
        str(sum(xs)),
        str(product(xs)),
        ''.join(map(str, xs)),
        ' '.join("Love is one damned thing after each other".split())
    ]))

if __name__ == "__main__":
    main()