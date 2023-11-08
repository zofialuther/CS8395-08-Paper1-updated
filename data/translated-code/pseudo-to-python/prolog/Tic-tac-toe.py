```python
import random

def tic_tac_toe_computer():
    V = random.randint(0, 8)
    TTT = [None, None, None, None, None, None, None, None, None]
    TTT[V] = 'o'
    display_tic_tac_toe(TTT)

def tic_tac_toe_me():
    TTT = [None, None, None, None, None, None, None, None, None]
    display_tic_tac_toe(TTT)

def display_tic_tac_toe(TTT):
    global box
    for i in range(9):
        box[i] = tic_tac_toe_box(TTT[i])

class tic_tac_toe_box:
    def __init__(self, lbl):
        self.mess = lbl

def play():
    L = list(range(9))
    TTT = [None, None, None, None, None, None, None, None, None]
    finished('x', TTT)

def finished(P, TTT):
    if winned(P, [TTT[0], TTT[1], TTT[2]]) or winned(P, [TTT[3], TTT[4], TTT[5]]) or winned(P, [TTT[6], TTT[7], TTT[8]]) or winned(P, [TTT[0], TTT[3], TTT[6]]) or winned(P, [TTT[1], TTT[4], TTT[7]]) or winned(P, [TTT[2], TTT[5], TTT[8]]) or winned(P, [TTT[0], TTT[4], TTT[8]]) or winned(P, [TTT[2], TTT[4], TTT[6]]):
        display_inform('You win !')
    elif allPositionsFilled(TTT):
        display_inform('Draw !')
    else:
        next_move(TTT)

def next_move(TTT):
    minimax('o', 0, 1024, TTT)

def winned(P, TTT):
    if is_winning_line(P, [TTT[0], TTT[1], TTT[2]]) or is_winning_line(P, [TTT[3], TTT[4], TTT[5]]) or is_winning_line(P, [TTT[6], TTT[7], TTT[8]]) or is_winning_line(P, [TTT[0], TTT[3], TTT[6]]) or is_winning_line(P, [TTT[1], TTT[4], TTT[7]]) or is_winning_line(P, [TTT[2], TTT[5], TTT[8]]) or is_winning_line(P, [TTT[0], TTT[4], TTT[8]]) or is_winning_line(P, [TTT[2], TTT[4], TTT[6]]):
        return True
    else:
        return False

def is_winning_line(P, line):
    if line[0] == P and line[1] == P and line[2] == P:
        return True
    else:
        return False

def allPositionsFilled(TTT):
    return None not in TTT

def display_inform(msg):
    print(msg)

def minimax(Player, Deep, Alpha, Beta, TTT):
    if eval(Player, Deep, TTT) is not None:
        return eval(Player, Deep, TTT)
    else:
        L = possible_move(TTT)
        bestVal = -1
        for TTT1 in L:
            Val = -minimax(otherPlayer(Player), Deep + 1, -Beta, -Alpha, TTT1)
            if Val > bestVal:
                bestVal = Val
                TT1 = TTT1
            Alpha = max(Alpha, Val)
            if Alpha >= Beta:
                break
        if Deep == 0:
            return TT1
        else:
            return bestVal

def eval(Player, Deep, TTT):
    if winned(Player, TTT):
        if Player == 'o':
            return 1000 - 50 * Deep
        else:
            return -1000 + 50 * Deep
    elif winned(otherPlayer(Player), TTT):
        if Player == 'x':
            return 1000 - 50 * Deep
        else:
            return -1000 + 50 * Deep
    elif allPositionsFilled(TTT):
        return 0
    else:
        return None

def possible_move(TTT):
    LMove = []
    for i in range(9):
        if TTT[i] is None:
            LMove.append(TTT[:i] + ['x'] + TTT[i+1:])
    return LMove

def otherPlayer(Player):
    if Player == 'x':
        return 'o'
    else:
        return 'x'
```