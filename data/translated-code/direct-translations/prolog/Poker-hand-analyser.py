```python
# utils/parser
def parse_line(Cards, line):
    return parse_line(Cards, line)

def parse_card(C):
    return parse_card(C)

def parse_suit(S, In, Out):
    if suit(S):
        return atom_codes(S, Xs) + Out + In

def parse_face(F, In, Out):
    if face(F):
        if number(F):
            return number_codes(F, Xs) + Out + In
        else:
            return atom_codes(F, Xs) + Out + In

def face_codes(F, Xs):
    if number(F):
        return number_codes(F, Xs)
    else:
        return atom_codes(F, Xs)

# tests
def test(line):
    return test(line)

def run_tests():
    for line in test:
        Cards = parse_line(line)
        H = best_hand(Cards)
        print(Cards, '\t', H)

def main():
    run_tests()
    #halt()  # not sure what this does in the original code

def faces():
    return ['a', 'k', 'q', 'j', 10, 9, 8, 7, 6, 5, 4, 3, 2]

def face(F):
    return F in faces()

def suit(S):
    return S in ['♥', '♦', '♣', '♠']

def best_hand(Cards):
    if straight_flush(Cards):
        return straight_flush(Cards)
    elif many_kind(Cards, 4):
        return four_of_a_kind()
    elif full_house(Cards):
        return full_house()
    elif flush(Cards):
        return flush()
    elif straight(Cards):
        return straight()
    elif many_kind(Cards, 3):
        return three_of_a_kind()
    elif two_pair(Cards):
        return two_pair()
    elif many_kind(Cards, 2):
        return one_pair()
    elif many_kind(Cards, 1):
        return high_card()
    else:
        return 'invalid'

def straight_flush(Cards):
    if straight(Cards):
        return flush(Cards)

def full_house(Cards):
    F1 = 0
    F2 = 0
    if many_kind(Cards, 3, F1) and many_kind(Cards, 2, F2) and F1 != F2:
        return True

def flush(Cards):
    return all(has_suit(S, Cards) for S in ['♥', '♦', '♣', '♠'])

def has_suit(S, Cards):
    return any(C.suit == S for C in Cards)

def straight(Cards):
    if len(Cards) == 0:
        return False
    else:
        F = Cards[0].face
        Cs = Cards[1:]
        F1 = pred_face(F)
        return straight(Cs, F1)

def pred_face(F):
    if F == 2:
        return 'a'
    else:
        Fs = faces()
        return Fs[Fs.index(F)-1]

def two_pair(Cards):
    F1 = 0
    F2 = 0
    if many_kind(Cards, 2, F1) and many_kind(Cards, 2, F2) and F1 != F2:
        return True

def many_kind(Cards, N, F):
    if face(F):
        Xs = [1 for c in Cards if c.face == F]
        return len(Xs) == N
```