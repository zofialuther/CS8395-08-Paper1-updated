```python
from itertools import combinations
from enum import Enum
import random

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
    def __init__(self, color, symbol, count, shading):
        self.color = color
        self.symbol = symbol
        self.count = count
        self.shading = shading

def isSet(cards):
    total = len(set([card.color for card in cards] + [card.symbol for card in cards] + [card.count for card in cards] + [card.shading for card in cards]))
    return 2 not in [total, total, total, total]

def getCard(deck):
    card = deck[0]
    new_deck = deck[1:]
    return card, new_deck

def getHand(n):
    deck = [Card(color, symbol, count, shading) for color in Color for symbol in Symbol for count in Count for shading in Shading]
    hand = []
    for _ in range(n):
        card, deck = getCard(deck)
        hand.append(card)
    return hand, deck

def getManyHands(n):
    while True:
        hand, _ = getHand(n)
        if isSet(hand):
            return hand

def showSolutions(hand_size, num_solutions):
    print(f"Hand size: {hand_size}")
    print(f"Number of solutions: {num_solutions}")
    random.seed()
    hand = getManyHands(hand_size)
    print(hand)
    solution_count = 0
    for combo in combinations(hand, 3):
        if isSet(combo):
            solution_count += 1
    print(f"Solutions: {solution_count}")

def main():
    showSolutions(9, 4)
    showSolutions(12, 6)
```