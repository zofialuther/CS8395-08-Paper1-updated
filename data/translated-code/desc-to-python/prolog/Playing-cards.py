```python
class Card:
    def __init__(self, pip, suit):
        self.pip = pip
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = [Card(pip, suit) for pip in range(1, 14) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def print_deck(self):
        for card in self.cards:
            print(f"{card.pip} of {card.suit}")
```