class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    
    def __repr__(self):
        return self.face + self.suit

suit = '♥ ♦ ♣ ♠'.split()
faces = '2 3 4 5 6 7 8 9 10 j q k a'
lowaces = 'a 2 3 4 5 6 7 8 9 10 j q k'
faces = faces.split()
lowaces = lowaces.split()

def straightflush(hand):
    if '2' in [card.face for card in hand]:
        f, fs = lowaces, lowaces
    else:
        f, fs = faces, faces
    hand.sort(key=lambda card: (f.index(card.face), suit.index(card.suit)))
    first, rest = hand[0], hand[1:]
    if all(card.suit == hand[0].suit for card in hand) and ''.join(card.face for card in hand) in fs:
        return 'straight-flush', hand[-1].face
    else:
        return False

def fourofakind(hand):
    # similar implementation to straightflush

def fullhouse(hand):
    # similar implementation to straightflush

def flush(hand):
    # similar implementation to straightflush

def straight(hand):
    # similar implementation to straightflush

def threeofakind(hand):
    # similar implementation to straightflush

def twopair(hand):
    # similar implementation to straightflush

def onepair(hand):
    # similar implementation to straightflush

def highcard(hand):
    # similar implementation to straightflush

handrankorder = (straightflush, fourofakind, fullhouse, flush, straight, threeofakind, twopair, onepair, highcard)

def rank(cards):
    hand = handy(cards)
    for func in handrankorder:
        rank = func(hand)
        if rank:
            break
    assert rank
    return rank

def handy(cards='2♥ 2♦ 2♣ k♣ q♦'):
    hand = []
    for card in cards.split():
        f, s = card[:-1], card[-1]
        assert f in faces and s in suit
        hand.append(Card(f, s))
    assert len(hand) == 5 and len(set(hand)) == 5
    return hand

if __name__ == '__main__':
    hands = ['2♥ 3♥ 4♥ 5♥ 6♥', '2♦ 2♠ 2♣ 2♥ 3♦', '10♦ j♦ q♦ k♦ a♦']
    print("HAND", "CATEGORY", "TIE-BREAKER")
    for cards in hands:
        r = rank(cards)
        print(cards, r[0], r[1])