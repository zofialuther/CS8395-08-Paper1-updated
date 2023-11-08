```python
def main():
    run_tests = [test(" 2♥  2♦ 2♣ k♣  q♦"), test(" 2♥  5♥ 7♦ 8♣  9♠"), test(" a♥  2♦ 3♣ 4♣  5♦"), test(" 2♥  3♥ 2♦ 3♣  3♦"), test(" 2♥  7♥ 2♦ 3♣  3♦"), test(" 2♥  7♥ 7♦ 7♣  7♠"), test("10♥  j♥ q♥ k♥  a♥"), test(" 4♥  4♠ k♠ 5♦ 10♠"), test(" q♣ 10♣ 7♣ 6♣  4♣")]
    for test in run_tests:
        Cards = test
        H = best_hand(Cards)
        print(Cards, end='\t')
        print(H)
    return

def run_tests():
    test(" 2♥  2♦ 2♣ k♣  q♦")
    test(" 2♥  5♥ 7♦ 8♣  9♠")
    test(" a♥  2♦ 3♣ 4♣  5♦")
    test(" 2♥  3♥ 2♦ 3♣  3♦")
    test(" 2♥  7♥ 2♦ 3♣  3♦")
    test(" 2♥  7♥ 7♦ 7♣  7♠")
    test("10♥  j♥ q♥ k♥  a♥")
    test(" 4♥  4♠ k♠ 5♦ 10♠")
    test(" q♣ 10♣ 7♣ 6♣  4♣")
    return

def face_codes(F, Xs):
    if isinstance(F, int):
        Xs = str(F)
    else:
        Xs = F
    return Xs

def parse_face(F, In, Out):
    if isinstance(F, int):
        Xs = str(F)
    else:
        Xs = F
    Out = In + Xs
    return Out

def parse_suit(S, In, Out):
    Xs = S
    Out = In + Xs
    return Out

def parse_card(C):
    return parse_face(C[0]) + parse_suit(C[1])

def parse_line():
    return []

def many_kind(Cards, F, N):
    Xs = [c for c in Cards if c[0] == F]
    return len(Xs)

def two_pair(Cards, F1, F2):
    Xs1 = many_kind(Cards, F1, 2)
    Xs2 = many_kind(Cards, F2, 2)
    return F1 != F2

def straight(Cards, F):
    Cs = [c for c in Cards if c[0] == F]
    return pred_face(F, F1)

def pred_face(F, F1):
    if F == 2:
        F1 = 'a'
    else:
        Fs = faces()
        F1 = Fs[Fs.index(F)+1]
    return F1

def has_suit(S, c):
    return c[1] == S

def flush(Cards, S):
    return all(has_suit(S, c) for c in Cards)

def full_house(Cards, F1, F2):
    Xs1 = many_kind(Cards, F1, 3)
    Xs2 = many_kind(Cards, F2, 2)
    return F1 != F2

def straight_flush(Cards, c):
    return straight(Cards, c[0]) and flush(Cards, c[1])

def best_hand(Cards):
    if straight_flush(Cards, c):
        H = 'straight-flush'
    elif many_kind(Cards, F, 4):
        H = 'four-of-a-kind'
    elif full_house(Cards, F1, F2):
        H = 'full-house'
    elif flush(Cards, S):
        H = 'flush'
    elif straight(Cards, F):
        H = 'straight'
    elif many_kind(Cards, F, 3):
        H = 'three-of-a-kind'
    elif two_pair(Cards, F1, F2):
        H = 'two-pair'
    elif many_kind(Cards, F, 2):
        H = 'one-pair'
    elif many_kind(Cards, F, 1):
        H = 'high-card'
    else:
        H = 'invalid'
    return H

def suit(S):
    return S in ['♥','♦','♣','♠']

def face(F):
    Fs = faces()
    return F in Fs

def faces():
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']

if __name__ == "__main__":
    main()
```