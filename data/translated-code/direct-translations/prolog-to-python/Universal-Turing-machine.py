def turing(Config, Rules, TapeIn, TapeOut):
    IS = call(Config)
    perform(Config, Rules, IS, ([], TapeIn), (Ls, Rs))
    Ls1 = list(reversed(Ls))
    TapeOut = Ls1 + Rs

def perform(Config, Rules, State, TapeIn, TapeOut):
    FS, RS, B, Symbols = call(Config)
    if State in FS:
        TapeOut = TapeIn
    elif State in RS:
        LeftIn, RightIn = TapeIn
        Symbol, RightRem = symbol(RightIn)
        if Symbol in Symbols:
            NewSymbol, Action, NewState = call(Rules, State, Symbol)
            if NewSymbol in Symbols:
                LeftOut, RightOut = action(Action, (LeftIn, [NewSymbol] + RightRem), B)
                perform(Config, Rules, NewState, (LeftOut, RightOut), TapeOut)

def symbol(Rs):
    if not Rs:
        return B, []
    else:
        return Rs[0], Rs[1:]

def action(Action, Tape, B):
    if Action == "left":
        return left(Lin, Rin, B)
    elif Action == "stay":
        return Tape
    elif Action == "right":
        return right(Lin, Rin, B)

def left(Ls, Rs, B):
    if not Ls:
        return [], [B] + Rs
    else:
        return [Ls[0]] + Rs, B

def right(L, Rs, B):
    if not Rs:
        return [B] + L, []
    else:
        return [Rs[0]] + L, B