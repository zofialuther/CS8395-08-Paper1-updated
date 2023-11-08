```python
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

def straight_flush(cards):
    # implementation of straight flush logic
    pass

def four_of_a_kind(cards):
    # implementation of four of a kind logic
    pass

def full_house(cards):
    # implementation of full house logic
    pass

def flush(cards):
    # implementation of flush logic
    pass

def straight(cards):
    # implementation of straight logic
    pass

def three_of_a_kind(cards):
    # implementation of three of a kind logic
    pass

def two_pair(cards):
    # implementation of two pair logic
    pass

def one_pair(cards):
    # implementation of one pair logic
    pass

def high_card(cards):
    # implementation of high card logic
    pass

def rank(cards):
    # implementation of rank logic
    pass

def handy(input_string):
    # implementation of parsing and validating input cards
    pass

# main section
example_hands = [
    "10H JH QH KH AH",
    "2D 3D 4D 5D 6D",
    "7S 7H 7D 5C 5H",
    # more example hands
]

for hand in example_hands:
    parsed_hand = handy(hand)
    print(f"The rank of {hand} is {rank(parsed_hand)}")
```
