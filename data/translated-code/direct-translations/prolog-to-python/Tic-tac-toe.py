```python
import random

class TicTacToeBox(pce.Box):
    def __init__(self, lbl):
        super().__init__()
        self.mess = lbl
        self.size = (50, 50)
        self.recogniser = pce.handler_group(pce.new_click_gesture('left', '', 'single', pce.send(self, 'my_click')))
    
    def my_click(self, b):
        self.set_val('x')
        play()

    def set_val(self, val):
        if self.mess == ' ':
            self.mess = val
            self.redraw()
            self.flush()

    def _redraw_area(self, a):
        super()._redraw_area(a)
        lbl = pce.new_string(self.mess)
        x, y, w, h = self.area
        self.draw_box(x, y, w, h)
        self.draw_text(lbl, pce.font('times', 'normal', 30), x, y, w, h, 'center', 'center')

def tic_tac_toe(computer):
    V = random.randint(0, 8)
    TTT = [' ' for _ in range(9)]
    TTT[V] = 'o'
    display_tic_tac_toe(TTT)

def display_tic_tac_toe(TTT):
    box.clear()
    tic_tac_toe_window.clear()
    D = pce.window('Tic-tac-Toe')
    D.size(170, 170)
    X, Y = 10, 10
    display(D, X, Y, 0, TTT)
    tic_tac_toe_window.assert(D)
    D.open()

def display(D, X, Y, N, TTT):
    if not TTT:
        return
    display_line(D, X, Y, N, TTT[:3])
    Y1 = Y + 50
    N3 = N + 3
    display(D, X, Y1, N3, TTT[3:])

def display_line(D, X, Y, N, line):
    if not line:
        return
    C = line[0] if line[0] is not None else ' '
    C1 = C if C is not None else ' '
    B = TicTacToeBox(C1)
    box.assert(N, B)
    D.display(B, pce.point(X, Y))
    X1 = X + 50
    N1 = N + 1
    display_line(D, X1, Y, N1, line[1:])

def play():
    L = list(range(9))
    TTT = [' ' for _ in range(9)]
    for i in L:
        init(i, TTT)
    finished('x', TTT, Val)
    if Val == 2:
        pce.send(pce.send(pce.send(pce.send('@display', 'inform'), 'You win !'), tic_tac_toe_window(D)), 'destroy')
    elif Val == 1:
        pce.send(pce.send('@display', 'inform'), 'Draw !')
        pce.send(tic_tac_toe_window(D), 'destroy')
    else:
        next_move(TTT, TT1)
        for i, v in enumerate(TT1):
            display(i, v)
        finished('o', TT1, V)
        if V == 2:
            pce.send(pce.send('@display', 'inform'), 'I win !')
            pce.send(tic_tac_toe_window(D), 'destroy')
        elif V == 1:
            pce.send(pce.send('@display', 'inform'), 'Draw !')
            pce.send(tic_tac_toe_window(D), 'destroy')

def next_move(TTT, TT1):
    minimax('o', 0, 1024, TTT, _V1- TT1)

def display(I, V):
    if V is not None:
        box(I).set_val(V)

def init(I, V):
    box(I).set_val(V)

def winned(P, TTT):
    return (is_winning_line(P, TTT[:3]) or
            is_winning_line(P, TTT[3:6]) or
            is_winning_line(P, TTT[6:]) or
            is_winning_line(P, TTT[::3]) or
            is_winning_line(P, TTT[1::3]) or
            is_winning_line(P, TTT[2::3]) or
            is_winning_line(P, TTT[::4]) or
            is_winning_line(P, TTT[2:7:2]))

def is_winning_line(P, line):
    return all(x == P for x in line if x is not None)

def eval(Player, Deep, TTT, V):
    if winned(Player, TTT):
        if Player == 'o':
            V = 1000 - 50 * Deep
        else:
            V = -1000 + 50 * Deep
    elif winned('o' if Player == 'x' else 'x', TTT):
        if Player == 'x':
            V = 1000 - 50 * Deep
        else:
            V = -1000 + 50 * Deep
    elif all(x is not None for x in TTT):
        V = 0

def possible_move(TTT):
    return [i for i, x in enumerate(TTT) if x is None]

def assign_move(P, TTT, N, TT1):
    TT1 = TTT[:]
    TT1[N] = P

def get_next(Player, Deep, TTT, Player1, Deep1, L):
    LMove = possible_move(TTT)
    Player1 = 'o' if Player == 'x' else 'x'
    Deep1 = Deep + 1
    L = [assign_move(Player, TTT, N, TT1) for N in LMove]

def finished(P, TTT, Val):
    if winned(P, TTT):
        Val = 2
    elif all(x is not None for x in TTT):
        Val = 1
    else:
        Val = 0

def computer(o):
    pass
```