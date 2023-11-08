```python
from typing import List, Tuple
import random
from enum import Enum


def combinations(k: int, lst: List) -> List[List]:
    if k == 0:
        return [[]]
    if not lst:
        return []
    y, *ys = lst
    return list(map(lambda x: [y] + x, combinations(k - 1, ys))) + combinations(k, ys)


class Color(Enum):
    Red = 1
    Green = 2
    Purple = 3


class Symbol(Enum):
    Oval = 1
    Squiggle = 2
    Diamond = 3


class Count(Enum):
    One = 1
    Two = 2
    Three = 3


class Shading(Enum):
    Solid = 1
    Open = 2
    Striped = 3


class Card:
    def __init__(self, color: Color, symbol: Symbol, count: Count, shading: Shading):
        self.color = color
        self.symbol = symbol
        self.count = count
        self.shading = shading

    def __repr__(self):
        return f"Card(color={self.color}, symbol={self.symbol}, count={self.count}, shading={self.shading})"


def isSet(cards: List[Card]) -> bool:
    total = lambda attr: len(set(getattr(card, attr) for card in cards))
    return not any(total(attr) == 2 for attr in ["color", "symbol", "count", "shading"])


def getCard() -> Tuple[Card, List[Card]]:
    gen, cs = random.getstate(), []
    i = random.randint(0, len(cs) - 1)
    a, b = cs[:i], cs[i+1:]
    return b[0], a + b


def getHand(n: int) -> List[Card]:
    gen = random.getstate()
    az = [e for e in Color]
    deck = [Card(co, sy, ct, sh) for co in az for sy in az for ct in az for sh in az]
    a, (newGen, _) = [getCard() for _ in range(n)], (gen, deck)
    return a


def getManyHands(n: int) -> List[List[Card]]:
    return [getHand(n) for _ in range(n)]


def showSolutions(cardCount: int, solutionCount: int) -> None:
    print(f"Showing hand of {cardCount} cards with {solutionCount} solutions.")
    z = next(filter(lambda x: len(list(filter(isSet, combinations(3, x))) == solutionCount), getManyHands(cardCount)))
    for hand in z:
        print(hand)
    print("Solutions:")
    for st in filter(isSet, combinations(3, z)):
        for card in st:
            print(card)
        print("")


def main() -> None:
    showSolutions(9, 4)
    showSolutions(12, 6)


if __name__ == "__main__":
    main()
```