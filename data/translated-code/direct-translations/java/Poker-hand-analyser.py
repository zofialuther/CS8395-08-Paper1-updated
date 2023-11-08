```python
class PokerHandAnalyzer:
    faces = "AKQJT98765432"
    suits = "HDSC"
    deck = buildDeck()

    @staticmethod
    def main():
        print("Regular hands:\n")
        for input in ["2H 2D 2S KS QD",
                      "2H 5H 7D 8S 9D",
                      "AH 2D 3S 4S 5S",
                      "2H 3H 2D 3S 3D",
                      "2H 7H 2D 3S 3D",
                      "2H 7H 7D 7S 7C",
                      "TH JH QH KH AH",
                      "4H 4C KC 5D TC",
                      "QC TC 7C 6C 4C",
                      "QC TC 7C 7C TD"]:
            print(PokerHandAnalyzer.analyzeHand(input.split(" ")))

        print("\nHands with wildcards:\n")
        for input in ["2H 2D 2S KS WW",
                      "2H 5H 7D 8S WW",
                      "AH 2D 3S 4S WW",
                      "2H 3H 2D 3S WW",
                      "2H 7H 2D 3S WW",
                      "2H 7H 7D WW WW",
                      "TH JH QH WW WW",
                      "4H 4C KC WW WW",
                      "QC TC 7C WW WW",
                      "QC TC 7H WW WW"]:
            print(PokerHandAnalyzer.analyzeHandWithWildcards(input.split(" ")))

    @staticmethod
    def analyzeHand(hand):
        if len(hand) != 5:
            return PokerHandAnalyzer.Score("invalid hand: wrong number of cards", -1, hand)

        if len(set(hand)) != len(hand):
            return PokerHandAnalyzer.Score("invalid hand: duplicates", -1, hand)

        faceCount = [0] * len(PokerHandAnalyzer.faces)
        straight = 0
        flush = 0
        for card in hand:
            face = PokerHandAnalyzer.faces.index(card[0])
            if face == -1:
                return PokerHandAnalyzer.Score("invalid hand: non existing face", -1, hand)
            straight |= (1 << face)

            faceCount[face] += 1

            if card[1] not in PokerHandAnalyzer.suits:
                return PokerHandAnalyzer.Score("invalid hand: non-existing suit", -1, hand)
            flush |= (1 << PokerHandAnalyzer.suits.index(card[1]))

        while straight % 2 == 0:
            straight >>= 1

        hasStraight = straight == 0b11111 or straight == 0b1111000000001
        hasFlush = (flush & (flush - 1)) == 0

        if hasStraight and hasFlush:
            return PokerHandAnalyzer.Score("straight-flush", 9, hand)

        total = 0
        for count in faceCount:
            if count == 4:
                return PokerHandAnalyzer.Score("four-of-a-kind", 8, hand)
            if count == 3:
                total += 3
            elif count == 2:
                total += 2

        if total == 5:
            return PokerHandAnalyzer.Score("full-house", 7, hand)

        if hasFlush:
            return PokerHandAnalyzer.Score("flush", 6, hand)

        if hasStraight:
            return PokerHandAnalyzer.Score("straight", 5, hand)

        if total == 3:
            return PokerHandAnalyzer.Score("three-of-a-kind", 4, hand)

        if total == 4:
            return PokerHandAnalyzer.Score("two-pair", 3, hand)

        if total == 2:
            return PokerHandAnalyzer.Score("one-pair", 2, hand)

        return PokerHandAnalyzer.Score("high-card", 1, hand)

    @staticmethod
    def analyzeHandWithWildcards(hand):
        if hand.count("WW") > 2:
            raise ValueError("too many wildcards")

        return PokerHandAnalyzer.WildScore(PokerHandAnalyzer.analyzeHandWithWildcardsR(hand, None), hand.copy())

    @staticmethod
    def analyzeHandWithWildcardsR(hand, best):
        for i in range(len(hand)):
            if hand[i] == "WW":
                for card in PokerHandAnalyzer.deck:
                    if card not in hand:
                        hand[i] = card
                        best = PokerHandAnalyzer.analyzeHandWithWildcardsR(hand, best)
                hand[i] = "WW"
                break
        result = PokerHandAnalyzer.analyzeHand(hand)
        if best is None or result.weight > best.weight:
            best = result
        return best

    @staticmethod
    def buildDeck():
        dck = ["" for _ in range(len(PokerHandAnalyzer.suits) * len(PokerHandAnalyzer.faces))]
        i = 0
        for s in PokerHandAnalyzer.suits:
            for f in PokerHandAnalyzer.faces:
                dck[i] = f + s
                i += 1
        return dck

    class Score:
        def __init__(self, n, w, h):
            self.weight = w
            self.name = n
            self.hand = h.copy() if h else h

        def __str__(self):
            return str(self.hand) + " " + self.name

    class WildScore:
        def __init__(self, s, w):
            self.score = s
            self.wild = w.copy()

        def __str__(self):
            return f"{self.wild}\n{str(self.score)}"


PokerHandAnalyzer.main()
```