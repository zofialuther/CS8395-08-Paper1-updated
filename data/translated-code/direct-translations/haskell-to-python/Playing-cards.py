import random

class Pip:
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

class Suit:
    Diamonds = "Diamonds"
    Spades = "Spades"
    Hearts = "Hearts"
    Clubs = "Clubs"

Card = (Pip, Suit)

def fullRange():
    return list(range(min(Pip), max(Pip)+1))

def fullDeck():
    return [(pip, suit) for pip in fullRange() for suit in [Suit.Diamonds, Suit.Spades, Suit.Hearts, Suit.Clubs]]

def insertAt(n, x, ys):
    if n == 0:
        return [x] + ys
    elif len(ys) == 0:
        raise ValueError("insertAt: list too short")
    else:
        return [ys[0]] + insertAt(n-1, x, ys[1:])

def shuffle(g, xs):
    return shuffleHelper(g, xs, 0, [])

def shuffleHelper(g, xs, n, ys):
    if len(xs) == 0:
        return ys
    else:
        k, g_prime = random.randint(0, n), g
        return shuffleHelper(g_prime, xs[1:], n+1, insertAt(k, xs[0], ys))