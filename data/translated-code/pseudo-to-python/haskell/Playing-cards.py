import random

Pip = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
Suit = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

fullRange = list(range(len(Pip)))

fullDeck = [(pip, suit) for pip in fullRange for suit in fullRange]

def insertAt(n, x, ys):
    if n == 0:
        return [x] + ys
    elif not ys:
        raise IndexError("insertAt: list too short")
    else:
        return [ys[0]] + insertAt(n - 1, x, ys[1:])

def shuffle(g, xs):
    return shuffleHelper(g, xs, 0, [])

def shuffleHelper(g, xs, n, ys):
    if not xs:
        return ys
    else:
        k, g_ = random.randint(0, n), random.Random()
        return shuffleHelper(g_, xs[1:], n + 1, insertAt(k, xs[0], ys))