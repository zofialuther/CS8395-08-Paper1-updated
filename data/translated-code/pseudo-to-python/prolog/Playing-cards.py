def new_deck(Deck):
    Suits = ['clubs', 'hearts', 'spades', 'diamonds']
    Pips = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
    Deck = [(Pip, Suit) for Suit in Suits for Pip in Pips]

import random

def deck_shuffle(Deck, NewDeck):
    NumCards = len(Deck)
    Ord = [random.randint(1, 1000) for _ in range(NumCards)]
    Pairs = dict(zip(Ord, Deck))
    OrdPairs = {k: v for k, v in sorted(Pairs.items())}
    NewDeck = list(OrdPairs.values())

def deck_deal(Deck, Card, Cards):
    Card = Deck[0]
    Cards = Deck[1:]

def print_deck(Deck):
    for card in Deck:
        print_card(card)

def print_card(card):
    Pip, Suit = card
    print(f'{Pip} of {Suit}')