```python
import random

class SetPuzzle:

    class Color:
        def __init__(self, val):
            self.val = val

    class Number:
        def __init__(self, val):
            self.val = val

    class Symbol:
        def __init__(self, val):
            self.val = val

    class Fill:
        def __init__(self, val):
            self.val = val

    class Card:
        def __init__(self, c, n, s, f):
            self.c = c
            self.n = n
            self.s = s
            self.f = f

        def __str__(self):
            return f"[Card: {self.c}, {self.n}, {self.s}, {self.f}]"

    def __init__(self):
        self.deck = [None] * 81
        self.colors = [self.Color(i) for i in range(3)]
        self.numbers = [self.Number(i) for i in range(3)]
        self.symbols = [self.Symbol(i) for i in range(3)]
        self.fillmodes = [self.Fill(i) for i in range(3)]

    def main(self, numCards):
        self.deck = [None] * 81
        for i in range(81):
            self.deck[i] = self.Card(self.colors[i // 27], self.numbers[(i // 9) % 3], self.symbols[(i // 3) % 3], self.fillmodes[i % 3])
        self.findSets(numCards)

    def findSets(self, numCards):
        target = numCards // 2
        sets = [[] for _ in range(target)]
        cnt = 0
        while cnt != target:
            random.shuffle(self.deck)
            cards = self.deck[:numCards]
            for i in range(len(cards)-2):
                for j in range(i+1, len(cards)-1):
                    for k in range(j+1, len(cards)):
                        if self.validSet(cards[i], cards[j], cards[k]):
                            if cnt < target:
                                sets[cnt] = [cards[i], cards[j], cards[k]]
                            cnt += 1
                            if cnt > target:
                                break
        cards.sort(key=lambda x: (x.c.val, x.n.val))
        print(f"GIVEN {numCards} CARDS:\n")
        for c in cards:
            print(c)
        print("\nFOUND", target, "SETS:\n")
        for s in sets:
            for c in s:
                print(c)
            print()

    def validSet(self, c1, c2, c3):
        tot = (c1.c.val + c2.c.val + c3.c.val) % 3
        tot += (c1.n.val + c2.n.val + c3.n.val) % 3
        tot += (c1.s.val + c2.s.val + c3.s.val) % 3
        tot += (c1.f.val + c2.f.val + c3.f.val) % 3
        return tot == 0

SetPuzzle().main(12)
```