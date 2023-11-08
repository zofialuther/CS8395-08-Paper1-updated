def nonogram(RowSpec, ColSpec, Grid):
    rows(RowSpec, Grid)
    transpose(Grid, GridT)
    rows(ColSpec, GridT)

def rows([], []):
    return

def rows([C|Cs], [R|Rs]):
    row(C, R)
    rows(Cs, Rs)

def row(Ks, Row):
    sum(Ks, #=, Ones)
    sum(Row, #=, Ones)
    arcs(Ks, Arcs, start, Final)
    append(Row, [0], RowZ)
    automaton(RowZ, [source(start), sink(Final)], [arc(start,0,start) | Arcs])

def arcs([], [], Final, Final):
    return

def arcs([K|Ks], Arcs, CurState, Final):
    NextState = gensym(state, NextState)
    if (K == 0):
        Arcs = [arc(CurState,0,CurState), arc(CurState,0,NextState) | Rest]
        arcs(Ks, Rest, NextState, Final)
    else:
        Arcs = [arc(CurState,1,NextState) | Rest]
        K1 = K-1
        arcs([K1|Ks], Rest, NextState, Final)

def make_grid(Grid, X, Y, Vars):
    length(Grid,X)
    make_rows(Grid, Y, Vars)

def make_rows([], _, []):
    return

def make_rows([R|Rs], Len, Vars):
    length(R, Len)
    make_rows(Rs, Len, Vars0)
    append(R, Vars0, Vars)

def print([]):
    return

def print([R|Rs]):
    print_row(R)
    print(Rs)

def print_row([]):
    nl

def print_row([X|R]):
    if (X == 0):
        write(' ')
    else:
        write('x')
    print_row(R)

def nonogram(Rows, Cols):
    length(Rows, X)
    length(Cols, Y)
    make_grid(Grid, X, Y, Vars)
    nono(Rows, Cols, Grid)
    label(Vars)
    print(Grid)