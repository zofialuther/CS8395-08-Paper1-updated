def main():
    print("Regular hands:\n")
    for input in ["2H 2D 2S KS QD", "2H 5H 7D 8S 9D", "AH 2D 3S 4S 5S", "2H 3H 2D 3S 3D", "2H 7H 2D 3S 3D", "2H 7H 7D 7S 7C", "TH JH QH KH AH", "4H 4C KC 5D TC", "QC TC 7C 6C 4C", "QC TC 7C 7C TD"]:
        print(analyzeHand(input.split(" ")))
    print("\nHands with wildcards:\n")
    for input in ["2H 2D 2S KS WW", "2H 5H 7D 8S WW", "AH 2D 3S 4S WW", "2H 3H 2D 3S WW", "2H 7H 2D 3S WW", "2H 7H 7D WW WW", "TH JH QH WW WW", "4H 4C KC WW WW", "QC TC 7C WW WW", "QC TC 7H WW WW"]:
        print(analyzeHandWithWildcards(input.split(" ")))

def analyzeHand(hand):
    if len(hand) != 5:
        return Score("invalid hand: wrong number of cards", -1, hand)
    if len(set(hand)) != len(hand):
        return Score("invalid hand: duplicates", -1, hand)
    faceCount = [0] * len(faces)
    straight = 0
    flush = 0
    for card in hand:
        face = faces.index(card[0])
        if face == -1:
            return Score("invalid hand: non existing face", -1, hand)
        straight |= (1 << face)
        faceCount[face] += 1
        if card[1] not in suits:
            return Score("invalid hand: non-existing suit", -1, hand)
        flush |= (1 << suits.index(card[1]))
    while straight % 2 == 0:
        straight >>= 1
    hasStraight = straight == 0b11111 or straight == 0b1111000000001
    hasFlush = (flush & (flush - 1)) == 0
    if hasStraight and hasFlush:
        return Score("straight-flush", 9, hand)
    total = 0
    for count in faceCount:
        if count == 4:
            return Score("four-of-a-kind", 8, hand)
        if count == 3:
            total += 3
        elif count == 2:
            total += 2
    if total == 5:
        return Score("full-house", 7, hand)
    if hasFlush:
        return Score("flush", 6, hand)
    if hasStraight:
        return Score("straight", 5, hand)
    if total == 3:
        return Score("three-of-a-kind", 4, hand)
    if total == 4:
        return Score("two-pair", 3, hand)
    if total == 2:
        return Score("one-pair", 2, hand)
    return Score("high-card", 1, hand)

def analyzeHandWithWildcards(hand):
    if hand.count("WW") > 2:
        raise ValueError("too many wildcards")
    return WildScore(analyzeHandWithWildcardsR(hand, None), hand.copy())

def analyzeHandWithWildcardsR(hand, best):
    for i in range(len(hand)):
        if hand[i] == "WW":
            for card in deck:
                if card not in hand:
                    hand[i] = card
                    best = analyzeHandWithWildcardsR(hand, best)
            hand[i] = "WW"
            break
    result = analyzeHand(hand)
    if best is None or result.weight > best.weight:
        best = result
    return best

def buildDeck():
    dck = [None] * (len(suits) * len(faces))
    i = 0
    for s in suits:
        for f in faces:
            dck[i] = f + s
            i += 1
    return dck