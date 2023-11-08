```python
from pokerhand import Card
import random

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in range(1, 14) for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']]
    
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
    
if __name__ == "__main__":
    deck = Deck()
    for _ in range(8):
        for _ in range(5):
            print(deck.deal(), end=" ")
        print()
    
    print(deck.cards)
```