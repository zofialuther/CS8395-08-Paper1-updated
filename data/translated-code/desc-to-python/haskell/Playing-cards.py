class Pip:
    def __init__(self, value):
        self.value = value

class Suit:
    def __init__(self, name):
        self.name = name

class Card:
    def __init__(self, pip, suit):
        self.pip = pip
        self.suit = suit

def generate_pips():
    pips = []
    # Add code to generate pips
    return pips

def generate_suits():
    suits = []
    # Add code to generate suits
    return suits

def generate_deck():
    deck = []
    pips = generate_pips()
    suits = generate_suits()
    for pip in pips:
        for suit in suits:
            card = Card(pip, suit)
            deck.append(card)
    return deck

import random

def shuffle_deck(deck):
    # Fisher-Yates shuffle algorithm
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]
    return deck