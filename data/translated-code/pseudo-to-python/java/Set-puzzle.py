class SetPuzzle:

    class Color:
        GREEN = 0
        PURPLE = 1
        RED = 2

    class Number:
        ONE = 0
        TWO = 1
        THREE = 2

    class Symbol:
        OVAL = 0
        DIAMOND = 1
        SQUIGGLE = 2

    class Fill:
        OPEN = 0
        STRIPED = 1
        SOLID = 2

    class Card:
        def __init__(self, c, n, s, f):
            self.c = c
            self.n = n
            self.s = s
            self.f = f

        def __repr__(self):
            return f'[Card: {self.c}, {self.n}, {self.s}, {self.f}]'

        def __lt__(self, other):
            return (self.c - other.c) * 10 + (self.n - other.n)

    deck = []

    def main(self):
        self.deck = [self.Card(c, n, s, f) for c in range(3) for n in range(3) for s in range(3) for f in range(3)]
        self.findSets(12)

    def findSets(self, numCards):
        import random
        target = numCards // 2
        sets = []
        cnt = 0
        while cnt != target:
            random.shuffle(self.deck)
            cards = self.deck[:numCards]
            for i in range(len(cards) - 2):
                for j in range(i + 1, len(cards) - 1):
                    for k in range(j + 1, len(cards)):
                        if self.validSet(cards[i], cards[j], cards[k]):
                            if cnt < target:
                                sets.append([cards[i], cards[j], cards[k]])
                            cnt += 1
                            if cnt > target:
                                break
        cards.sort()
        print(f'GIVEN {numCards} CARDS:\n')
        for c in cards:
            print(c)
        print('\nFOUND', target, 'SETS:\n')
        for s in sets:
            for c in s:
                print(c)
            print()

    def validSet(self, c1, c2, c3):
        tot = 0
        tot += (c1.c + c2.c + c3.c) % 3
        tot += (c1.n + c2.n + c3.n) % 3
        tot += (c1.s + c2.s + c3.s) % 3
        tot += (c1.f + c2.f + c3.f) % 3
        return tot == 0

puzzle = SetPuzzle()
puzzle.main()