def turing(Config, Rules, TapeIn, TapeOut):
    call(Config, IS, _, _, _, _)
    perform(Config, Rules, IS, ([], TapeIn), (Ls, Rs))
    Ls1 = list(reversed(Ls))
    TapeOut = Ls1 + Rs

def perform(Config, Rules, State, TapeIn, TapeOut):
    call(Config, _, FS, RS, B, Symbols)
    if State in FS:
        TapeOut = TapeIn
    elif State in RS:
        LeftIn, RightIn = TapeIn
        Symbol, RightRem, B = symbol(RightIn)
        if Symbol in Symbols:
            NewSymbol, Action, NewState = call(Rules, State, Symbol)
            if NewSymbol in Symbols:
                LeftOut, RightOut = action(Action, LeftIn, [NewSymbol]+RightRem, B)
                perform(Config, Rules, NewState, (LeftOut, RightOut), TapeOut)

def symbol(tape):
    if not tape:
        return B, [], B
    else:
        return tape[0], tape[1:], _

def action(action, left, right, B):
    if action == 'left':
        return left(left, right, B)
    elif action == 'stay':
        return left
    elif action == 'right':
        return right(left, right, B)

def left(Lin, Rin, B):
    if not Lin:
        return [], [B]+Rin
    else:
        return Lin[1:], [Lin[0]]+Rin

def right(L, Rin, B):
    if not Rin:
        return [B]+L, []
    else:
        return [Rin[0]]+L, Rin[1:]