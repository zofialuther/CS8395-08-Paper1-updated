```python
# Cards module

from random import shuffle

def new_deck():
    suits = ['clubs', 'hearts', 'spades', 'diamonds']
    pips = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    return [ (pip, suit) for suit in suits for pip in pips ]

def deck_shuffle(deck):
    shuffle(deck)
    return deck

def deck_deal(deck):
    return deck[0], deck[1:]

def print_deck(deck):
    for card in deck:
        print_card(card)

def print_card(card):
    pip, suit = card
    print(f"{pip} of {suit}")
```