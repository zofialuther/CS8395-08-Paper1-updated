```python
from pokerhand import Card
import itertools
import random

class Deck:
    def __init__(self):
        self.__deck = [Card(face, suit) for face, suit in itertools.product(['2','3','4','5','6','7','8','9','10','J','Q','K','A'],['Hearts','Diamonds','Clubs','Spades'])]

    def __repr__(self):
        return 'Deck of ' + ' '.join(repr(card) for card in self.__deck)

    def shuffle(self):
        random.shuffle(self.__deck)

    def deal(self):
        return self.__deck.pop(random.randint(0, len(self.__deck)-1))

if __name__ == '__main__':
    deck = Deck()
    print('40 cards from a deck:')
    for _ in range(5):
        for _ in range(8):
            print(deck.deal())
        print()
    print('The remaining cards are a', deck)
```