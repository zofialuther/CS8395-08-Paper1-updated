```python
# Python code
import random

class Card:
    def __init__(self, color, number, symbol, fill):
        self.color = color
        self.number = number
        self.symbol = symbol
        self.fill = fill

def initializeDeck():
    deck = []
    colors = ["red", "green", "purple"]
    numbers = [1, 2, 3]
    symbols = ["diamond", "squiggle", "oval"]
    fills = ["solid", "striped", "empty"]
    for color in colors:
        for number in numbers:
            for symbol in symbols:
                for fill in fills:
                    deck.append(Card(color, number, symbol, fill))
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)

def findValidSets(deck):
    for i in range(len(deck)):
        for j in range(i+1, len(deck)):
            for k in range(j+1, len(deck)):
                if validSet(deck[i], deck[j], deck[k]):
                    print("Valid set found:", deck[i].color, deck[i].number, deck[i].symbol, deck[i].fill, 
                          deck[j].color, deck[j].number, deck[j].symbol, deck[j].fill, 
                          deck[k].color, deck[k].number, deck[k].symbol, deck[k].fill)

def validSet(card1, card2, card3):
    if (card1.color + card2.color + card3.color) % 3 == 0 and \
       (card1.number + card2.number + card3.number) % 3 == 0 and \
       (card1.symbol + card2.symbol + card3.symbol) % 3 == 0 and \
       (card1.fill + card2.fill + card3.fill) % 3 == 0:
        return True
    else:
        return False

deck = initializeDeck()
shuffleDeck(deck)
findValidSets(deck)
```